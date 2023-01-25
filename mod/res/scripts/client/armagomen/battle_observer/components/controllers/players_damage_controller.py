from collections import defaultdict

from Event import SafeEvent
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider


class PlayersDamageController(object):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        self.onPlayerDamaged = SafeEvent()
        self.playersDamage = defaultdict(int)
        self.inited = False

    def init(self):
        if self.inited:
            return
        self.inited = True
        self.playersDamage.clear()
        arena = self.sessionProvider.arenaVisitor.getArenaSubscription()
        if arena is not None:
            arena.onVehicleHealthChanged += self.onVehicleHealthChanged

    def fini(self):
        if not self.inited:
            return
        arena = self.sessionProvider.arenaVisitor.getArenaSubscription()
        if arena is not None:
            arena.onVehicleHealthChanged -= self.onVehicleHealthChanged
        self.inited = False

    def onVehicleHealthChanged(self, targetID, attackerID, damage):
        self.playersDamage[attackerID] += damage
        self.onPlayerDamaged(attackerID, self.playersDamage[attackerID])

    def getPlayerDamage(self, vehicleID):
        return self.playersDamage[vehicleID]


damage_controller = PlayersDamageController()