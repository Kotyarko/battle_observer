from armagomen.constants import SWF, ALIASES
from armagomen.utils.common import logError, logDebug, callback, logInfo
from armagomen.utils.events import g_events
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ComponentSettings, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE


def getViewSettings():
    from armagomen.battle_observer.lobby.date_times import DateTimes
    return (ComponentSettings(ALIASES.DATE_TIME, DateTimes, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return ObserverBusinessHandlerLobby(),


def getContextMenuHandlers():
    return ()


class ObserverBusinessHandlerLobby(PackageBusinessHandler):
    __slots__ = ('_listeners', '_scope', '_app', '_appNS', '__loaded')

    def __init__(self):
        listeners = [(VIEW_ALIAS.LOBBY_HANGAR, self.eventListener), (VIEW_ALIAS.LOGIN, self.eventListener)]
        super(ObserverBusinessHandlerLobby, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
        self.__loaded = False

    def eventListener(self, event):
        self._app.loaderManager.onViewLoaded += self._onViewLoaded
        if event.alias == VIEW_ALIAS.LOBBY_HANGAR and not self.__loaded:
            self._app.as_loadLibrariesS([SWF.LOBBY])
            logInfo("{}: loading libraries swf={}, alias={}".format(self.__class__.__name__, SWF.LOBBY, event.alias))
            self.__loaded = True

    @staticmethod
    def load(view):
        g_events.onHangarLoaded(view)
        if hasattr(view.flashObject, SWF.ATTRIBUTE_NAME):
            view.flashObject.as_observerCreateComponents([ALIASES.DATE_TIME])
        else:
            logError("hangar_page {}, has ho attribute {}", view.settings.alias, SWF.ATTRIBUTE_NAME)

    def _onViewLoaded(self, view, *args):
        alias = view.getAlias()
        if alias == VIEW_ALIAS.LOGIN:
            callback(1.0, g_events.onLoginLoaded, view)
            logDebug("onViewLoaded, alias={}", alias)
        elif alias == VIEW_ALIAS.LOBBY_HANGAR:
            callback(1.0, self.load, view)
            logDebug("onViewLoaded, alias={}", alias)
