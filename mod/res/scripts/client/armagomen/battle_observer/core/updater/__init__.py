import os
import re
from collections import namedtuple
from json import loads
from zipfile import ZipFile

from account_helpers.settings_core.settings_constants import GAME
from armagomen.battle_observer.core.updater.i18n import getI18n
from armagomen.constants import GLOBAL, URLS
from armagomen.utils.common import logInfo, logError, modsPath, gameVersion, getUpdatePath, fetchURL, logDebug, callback
from armagomen.utils.dialogs import UpdaterDialogs
from gui.Scaleform.Waiting import Waiting
from gui.shared.personality import ServicesLocator
from skeletons.gui.app_loader import GuiGlobalSpaceID
from uilogging.core.core_constants import HTTP_OK_STATUS
from web.cache.web_downloader import WebDownloader
from wg_async import wg_async, wg_await

WAITING_UPDATE = 'updating'

__NAMES = (
    'CHECK', 'UPDATE_CHECKED', 'NEW_VERSION', 'STARTED', 'NEW_FILE', 'ALREADY_DOWNLOADED', 'FINISHED', 'FAILED'
)
__MESSAGES = (
    'Checking for an available update.',
    'The update check is completed, you have the current version.',
    'An update {} is detected, the client will be restarted at the end of the download.',
    'DownloadThread: update started {} at {}',
    'DownloadThread: added new file {}',
    'DownloadThread: update is already downloaded to: {}',
    'DownloadThread: downloading update finished to: {}',
    'DownloadThread: update download failed: {}'
)

LOG_MESSAGES = namedtuple("MESSAGES", __NAMES)(*__MESSAGES)


class DownloadThread(object):
    URLS = {'auto': 'https://github.com/Armagomen/battle_observer/releases/latest/download/AutoUpdate.zip',
            'full': 'https://github.com/Armagomen/battle_observer/releases/latest/download/BattleObserver_WOT_EU.zip'}

    def __init__(self):
        self.version = None
        self.i18n = getI18n()
        self.updateData = dict()
        self.dialogs = UpdaterDialogs()
        self.downloader = None
        self.modPath = os.path.join(modsPath, gameVersion)

    def startDownload(self):
        Waiting.show(WAITING_UPDATE)
        mod_version = self.updateData.get('tag_name', self.version)
        path = os.path.join(getUpdatePath(), mod_version + ".zip")
        if os.path.isfile(path):
            self.extractZipArchive(path)
            logInfo(LOG_MESSAGES.ALREADY_DOWNLOADED.format(path))
            self.dialogs.showUpdateFinished(self.i18n['titleOK'], self.i18n['messageOK'].format(mod_version))
        else:
            url = self.URLS['auto']
            self.downloader = WebDownloader(GLOBAL.ONE)
            if url:
                logInfo(LOG_MESSAGES.STARTED.format(mod_version, url))
                self.downloader.download(url, self.onDownloaded)
            else:
                self.closeDownloader()
                self.downloadError(url)

    def closeDownloader(self):
        if self.downloader is not None:
            self.downloader.close()
            self.downloader = None

    def extractZipArchive(self, path):
        old_files = os.listdir(self.modPath)
        with ZipFile(path, "r") as archive:
            for newFile in archive.namelist():
                if newFile not in old_files:
                    archive.extract(newFile, self.modPath)
                    logInfo(LOG_MESSAGES.NEW_FILE.format(newFile))
        if Waiting.isOpened(WAITING_UPDATE):
            Waiting.hide(WAITING_UPDATE)

    def onDownloaded(self, _url, data):
        self.closeDownloader()
        if data is not None:
            mod_version = self.updateData.get('tag_name', self.version)
            path = os.path.join(getUpdatePath(), mod_version + ".zip")
            with open(path, "wb") as zipArchive:
                zipArchive.write(data)
            logInfo(LOG_MESSAGES.FINISHED.format(path))
            self.extractZipArchive(path)
            self.dialogs.showUpdateFinished(self.i18n['titleOK'], self.i18n['messageOK'].format(mod_version))
        else:
            self.downloadError(_url)

    def downloadError(self, url):
        if Waiting.isOpened(WAITING_UPDATE):
            Waiting.hide(WAITING_UPDATE)
        message = LOG_MESSAGES.FAILED.format(url)
        logError(message)
        self.dialogs.showUpdateError(message)


class Updater(DownloadThread):

    def __init__(self, version):
        super(Updater, self).__init__()
        self.version = version
        self.loginServerSelection = ServicesLocator.settingsCore.getSetting(GAME.LOGIN_SERVER_SELECTION)
        self.updateAvailable = None
        ServicesLocator.appLoader.onGUISpaceEntered += self.onGUISpaceEntered
        fetchURL(URLS.UPDATE_GITHUB_API_URL, self.request_last_version)
        logInfo(LOG_MESSAGES.CHECK)

    def request_last_version(self, response):
        if response.responseCode == HTTP_OK_STATUS:
            response_data = loads(response.body)
            self.updateData.update(response_data)
            new_version = response_data.get('tag_name', self.version)
            local_ver = self.tupleVersion(self.version)
            server_ver = self.tupleVersion(new_version)
            if local_ver < server_ver:
                assets = response_data.get('assets')
                for asset in assets:
                    filename = asset.get('name', '')
                    download_url = asset.get('browser_download_url')
                    if filename == 'AutoUpdate.zip':
                        self.URLS['auto'] = download_url
                    elif filename == 'BattleObserver_WOT_EU.zip':
                        self.URLS['full'] = download_url
                logInfo(LOG_MESSAGES.NEW_VERSION.format(new_version))
            else:
                logInfo(LOG_MESSAGES.UPDATE_CHECKED)
            self.updateAvailable = local_ver < server_ver
        else:
            callback(120.0, fetchURL, URLS.UPDATE_GITHUB_API_URL, self.request_last_version)
        logDebug('contentType={}, responseCode={} body={}', response.contentType, response.responseCode, response.body)

    @staticmethod
    def tupleVersion(version):
        return tuple(map(int, version.split('.')))

    @wg_async
    def onGUISpaceEntered(self, spaceID):
        if self.updateAvailable is None or GuiGlobalSpaceID.LOGIN == spaceID and not self.loginServerSelection:
            return
        ServicesLocator.appLoader.onGUISpaceEntered -= self.onGUISpaceEntered
        if not self.updateAvailable:
            return
        title = self.i18n['titleNEW'].format(self.updateData.get('tag_name', self.version))
        git_message = re.sub(r'^\s+|\r|\t|\s+$', GLOBAL.EMPTY_LINE, self.updateData.get('body', GLOBAL.EMPTY_LINE))
        message = self.i18n['messageNEW'].format(self.modPath, git_message)
        result = yield wg_await(self.dialogs.showNewVersionAvailable(title, message, self.URLS['full']))
        if result:
            self.startDownload()
