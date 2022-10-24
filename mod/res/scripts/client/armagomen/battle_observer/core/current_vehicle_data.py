import math
from collections import namedtuple

from CurrentVehicle import g_currentVehicle
from PlayerEvents import g_playerEvents
from armagomen.utils.common import logError, logDebug
from constants import ROLE_TYPE

EfficiencyAVGData = namedtuple("EfficiencyAVGData", ("damage", "assist"))
DEBUG_STRING = "set vehicle cache: name={} avgDamage={}, avgAssist={}, isSPG={}"


class CurrentVehicleCachedData(object):

    def __init__(self):
        self.__isSPG = False
        self.__EfficiencyAVGData = EfficiencyAVGData(0, 0)

    def init(self):
        g_playerEvents.onArenaCreated += self.onArenaCreated

    def fini(self):
        g_playerEvents.onArenaCreated -= self.onArenaCreated

    def onArenaCreated(self):
        self.__isSPG = False
        damage = 0
        assist = 0
        try:
            self.__isSPG = g_currentVehicle.item.role == ROLE_TYPE.SPG
            dossier = g_currentVehicle.getDossier()
            if dossier:
                random = dossier.getRandomStats()
                d_damage = random.getAvgDamage()
                d_assist = random.getDamageAssistedEfficiency()
                if d_damage is not None:
                    damage = int(math.floor(d_damage))
                if d_assist is not None:
                    assist = int(math.floor(d_assist))
        except Exception as error:
            logError(repr(error))
        finally:
            self.__EfficiencyAVGData = EfficiencyAVGData(damage, assist)
        logDebug(DEBUG_STRING, g_currentVehicle.item.userName, damage, assist, self.__isSPG)

    @property
    def efficiencyAvgData(self):
        return self.__EfficiencyAVGData

    @property
    def isSPG(self):
        return self.__isSPG
