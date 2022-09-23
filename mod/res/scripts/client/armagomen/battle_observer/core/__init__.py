__version__ = "1.39.3"

from debug_utils import LOG_CURRENT_EXCEPTION

loadError = False
errorMessage = ""

try:
    from armagomen.battle_observer.core.updater import Updater

    updater = Updater(__version__)
except Exception:
    LOG_CURRENT_EXCEPTION()

try:
    from armagomen.battle_observer.components import ComponentsLoader
    from armagomen.battle_observer.core.view_settings import ViewSettings
    from armagomen.battle_observer.settings.hangar.hangar_settings import SettingsInterface
    from armagomen.battle_observer.settings.loader import SettingsLoader
    from armagomen.utils.common import isFileValid, clearClientCache, cleanupUpdates, logInfo, logError, gameVersion
    from sys import version as pythonVersion
except Exception as err:
    LOG_CURRENT_EXCEPTION()
    loadError = True
    errorMessage = repr(err)
else:
    if isFileValid(__version__):
        logInfo('Launched at python v{}'.format(pythonVersion))
        logInfo('MOD START LOADING: v{} - {}'.format(__version__, gameVersion))
        _view_settings = ViewSettings()
        componentsLoader = ComponentsLoader()
        settings_loader = SettingsLoader()
        hangar_settings = SettingsInterface(settings_loader, __version__)
    else:
        loadError = True
        URL = 'https://github.com/Armagomen/battle_observer/releases/latest'
        errorMessage = 'ERROR: file armagomen.battleObserver_{}.wotmod is not valid, mod locked, please ' \
                       'install mod from official source: {}'.format(__version__, URL)
        logError(errorMessage)


def init():
    if loadError:
        from armagomen.battle_observer.core.loading_error import LoadingError
        return LoadingError(errorMessage)


def fini():
    if loadError:
        return
    clearClientCache()
    cleanupUpdates()
    logInfo('MOD SHUTTING DOWN: v{} - {}'.format(__version__, gameVersion))
