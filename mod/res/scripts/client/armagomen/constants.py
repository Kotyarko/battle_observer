from collections import namedtuple

import ResMgr

from account_helpers.settings_core.settings_constants import GAME
from aih_constants import CTRL_MODE_NAME
from gui.Scaleform.daapi.view.battle.shared.crosshair.settings import SHOT_RESULT_TO_DEFAULT_COLOR, \
    SHOT_RESULT_TO_ALT_COLOR
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME

MOD_NAME = "BATTLE_OBSERVER"
IMAGE_DIR = "gui/maps/icons/battle_observer"

SWF = namedtuple("SWF", "BATTLE LOBBY BATTLE_PACKAGES LOBBY_PACKAGES ATTRIBUTE_NAME")(
    'modBattleObserver.swf', 'modBattleObserverHangar.swf', ("armagomen.battle_observer.battle",),
    ("armagomen.battle_observer.lobby",), 'as_observerCreateComponents')


def getLogo(big=True):
    if big:
        return "<img src='img://{}/logo/big.png' width='500' height='32' vspace='16'>".format(IMAGE_DIR)
    return "<img src='img://{}/logo/small.png' width='220' height='14' vspace='16'>".format(IMAGE_DIR)


def sixthSenseIconsNamesList():
    directory = IMAGE_DIR + "/sixth_sense/"
    folder = ResMgr.openSection(directory)
    return sorted(folder.keys())


IMG = namedtuple("IMG", "DONAT_UA PATREON PAYPAL QR")(
    "<img src='img://{}/donate/donatua.png' width='16' height='16' vspace='-3'>".format(IMAGE_DIR),
    "<img src='img://{}/donate/patreon.png' width='16' height='16' vspace='-3'>".format(IMAGE_DIR),
    "<img src='img://{}/donate/paypal.png' width='16' height='16' vspace='-3'>".format(IMAGE_DIR),
    "<img src='img://{}/donate/donate-qr.png' width='212' height='212' vspace='0'>".format(IMAGE_DIR)
)

URLS = namedtuple("URLS", (
    "DONATE_UA_URL",
    "PAYPAL_URL",
    "UPDATE_GITHUB_API_URL",
    "PATREON_URL",
    "DISCORD"
))("https://donatua.com/@armagomen",
   "https://www.paypal.com/donate/?hosted_button_id=VJCUNYNBXBEG8",
   "https://api.github.com/repos/Armagomen/battle_observer/releases/latest",
   "https://www.patreon.com/armagomen",
   "https://discord.gg/Nma5T5snKW")

VEHICLE = namedtuple("VEHICLE", ("CUR", "MAX", "TEAM", "PERCENT", "VEHICLE"))(
    "health", "maxHealth", "team", "percent", "Vehicle")
REGIONS = namedtuple("REGIONS", ("EU", "ASIA", "NA"))("eu", "asia", "com")


class GLOBAL:
    def __init__(self):
        pass

    ALIGN = "align"
    ALIGN_LIST = namedtuple("ALIGN_LIST", ("left", "center", "right"))("left", "center", "right")
    ALPHA = "alpha"
    AVG_COLOR = "avgColor"
    BG_ALPHA = "bgAlpha"
    BLUR_X = "blurX"
    BLUR_Y = "blurY"
    COLOR = "color"
    COMMA_SEP = ", "
    CONFIG_ERROR = "macros not found"
    CUSTOM_COLOR = "customColor"
    C_INTERFACE_SPLITTER = "*"
    EMPTY_LINE = ""
    ENABLED = "enabled"
    FIRST, LAST = (0, -1)
    F_ONE = 1.0
    GLOW_FILTER = "glowFilter"
    HEIGHT = "height"
    ICONS_DIR = "img://gui/maps/icons"
    IMG = "img"
    IMG_PARAMS = {"dir": "img://gui/maps/icons/library/efficiency/48x48", "size": "width='24' height='24'",
                  "vspace": "vspace='-13'"}
    IMG_PARAMS_HANGAR = {"dir": "img://gui/maps/icons/library/efficiency/48x48", "size": "width='30' height='30'"}
    INNER = "inner"
    KNOCKOUT = "knockout"
    ONE, TWO = (1, 2)
    OUTLINE = "outline"
    SCALE = "scale"
    SETTINGS = "settings"
    SMOOTHING = "smoothing"
    STRENGTH = "strength"
    WIDTH = "width"
    X = "x"
    Y = "y"
    ZERO = FIRST
    NEW_LINE = "\n"


SERVICE_CHANNEL = namedtuple("SERVICE_CHANNEL", ("NAME", "KEYS", "TYPE", "DATA", "AUX_DATA", "SYSTEM_CHANNEL_KEYS"))(
    "service_channel_filter", "sys_keys", "type", "data", "auxData", (
        "CustomizationForCredits", "CustomizationForGold", "DismantlingForCredits",
        "DismantlingForCrystal", "DismantlingForGold", "Information", "MultipleSelling",
        "PowerLevel", "PurchaseForCredits", "Remove", "Repair", "Restore", "Selling",
        "autoMaintenance", "customizationChanged", "PurchaseForCrystal",
        "PurchaseForGold", "GameGreeting"))

__Main = namedtuple("MAIN", (
    "AUTO_CLEAR_CACHE", "HIDE_BADGES", "HIDE_CLAN_ABBREV", "HIDE_DOG_TAGS", "NAME", "SHOW_FRIENDS", "SHOW_ANONYMOUS",
    "USE_KEY_PAIRS", "IGNORE_COMMANDERS", "DISABLE_SCORE_SOUND", "DEBUG", "CREW_TRAINING", "DIRECTIVES", "HIDE_HINT",
    "FIELD_MAIL", "CREW_RETURN", "STUN_SOUND", "HIDE_MAIN_CHAT", "HIDE_BTN_COUNTERS", "PREMIUM_TIME", "SAVE_SHOT",
    "MUTE_BASES_SOUND"))
MAIN = __Main(
    "autoClearCache", "hideBadges", "hideClanAbbrev", "hide_dog_tags", "main", "showFriendsAndClanInEars",
    "anonymousEnableShow", "useKeyPairs", "ignore_commanders_voice", "disable_score_sound", "DEBUG_MODE",
    "auto_crew_training", "do_not_buy_directives_for_currency_automatically", "hide_hint_panel", "hide_field_mail",
    "auto_return_crew", "disable_stun_sound", "hide_main_chat_in_hangar", "hide_button_counters_on_top_panel",
    "premium_time", "save_shot", "mute_team_base_sound")

COLORS = namedtuple("COLORS", (
    "NAME", "BLACK", "BLIND", "B_SILVER", "GOLD", "GREEN", "NORMAL_TEXT", "ORANGE", "RED", "S_YELLOW", "YELLOW",
    "C_GREEN", "C_ORANGE", "C_RED", "C_YELLOW", "C_PURPLE", "C_BG", "GLOBAL", "ALLY_MAME", "ENEMY_MAME",
    "ENEMY_BLIND_MAME", "DEAD_COLOR"))(
    "colors", "#000000", "#6F6CD3", "#858585", "#FFD700", "#5ACB00", "#FAFAFA", "#FF9900", "#F30900", "#E0E06D",
    "#FFC900", "green", "orange", "red", "yellow", "purple", "bgColor", "global", "ally", "enemy", "enemyColorBlind",
    "deadColor")

MAIN_GUN = namedtuple("MAIN_GUN", (
    "NAME", "TEMPLATE", "GUN_ICON", "DONE_ICON", "FAILURE_ICON", "MIN_GUN_DAMAGE", "DAMAGE_RATE", "INFO"))(
    "main_gun", "template", "mainGunIcon", "mainGunDoneIcon", "mainGunFailureIcon", 1000, 0.2,
    "mainGun")

MINIMAP = namedtuple("MINIMAP", (
    "NAME", "DEATH_PERMANENT", "SHOW_NAMES", "ZOOM", "VIEW_RADIUS", "YAW", "ZOOM_KEY"))(
    "minimap", "permanentMinimapDeath", "showDeathNames", "zoom", "real_view_radius",
    "yaw_limits", "zoom_hotkey")

HP_BARS = namedtuple("HP_BARS", ("NAME", "STYLE", "WIDTH", "ALIVE", "STYLES"))(
    "hp_bars", "style", "barsWidth", "showAliveCount",
    namedtuple("HpStyles", ("normal", "league"))("normal", "league"))

CLOCK = namedtuple("CLOCK", (
    "NAME", "IN_BATTLE", "IN_LOBBY", "FORMAT", "UPDATE_INTERVAL", "DEFAULT_FORMAT_BATTLE", "DEFAULT_FORMAT_HANGAR"))(
    "clock", "battle", "hangar", "format", 1.0, "<textformat tabstops='[120]'>%d %b %Y<tab>%X</textformat>",
    "<textformat tabstops='[135]'>%d %b %Y<tab>%X</textformat>")

PREMIUM = namedtuple("PREMIUM", ("PREMIUM_TIME",))(
    "premium_time", )

__Sniper = namedtuple("SNIPER", (
    "ZOOM", "NAME", "DYN_ZOOM", "STEPS_ONLY", "ZOOM_STEPS", "STEPS", "METERS", "ZOOMS", "ZOOM_EXPOSURE",
    "INCREASED_ZOOM", "DEFAULT_STEPS", "EXPOSURE_FACTOR", "MAX_CALIBER", "MAX_DIST", "DISABLE_SNIPER",
    "DISABLE_LATENCY", "SKIP_CLIP", "CLIP", "MIN_ZOOM"))
SNIPER = __Sniper(
    "zoom", "zoom", "dynamic_zoom", "steps_only", "zoomSteps", "steps", "zoomXMeters", "zooms",
    "zoomExposure", "increasedZoom", [float(x) for x in xrange(2, 26, 2)], 0.1, 60, 570.0,
    "disable_cam_after_shot", "disable_cam_after_shot_latency", "disable_cam_after_shot_skip_clip", "clip", 2.0)


class DAMAGE_LOG:
    def __init__(self):
        pass

    NAME = "damage_log"
    TOP_LOG = "log_total"
    WG_LOGS_FIX = "wg_logs"

    EXTENDED = "log_extended"
    D_DONE, D_RECEIVED = (0, 1)

    D_DONE_ENABLED = "top_enabled"
    D_RECEIVED_ENABLED = "bottom_enabled"

    ALL_DAMAGES = "allDamages"
    ATTACK_REASON = "attackReason"
    CLASS_COLOR = "tankClassColor"
    CLASS_ICON = "classIcon"
    DAMAGE_LIST = "damageList"

    HOT_KEY = "logsAltMode_hotkey"
    ICONS = "icons"
    ICON_NAME = "iconName"
    INDEX = "index"
    IN_CENTER = "inCenter"
    KILLED_ICON = "killedIcon"
    LAST_DAMAGE = "lastDamage"
    LOG_MODE = ("extendedLog", "extendedLogALTMODE")
    NOT_SHELL = "--"
    PERCENT_AVG_COLOR = "percentDamageAvgColor"
    REVERSE = "reverse"
    SHELL = ("normal", "gold")
    SHELL_COLOR = "shellColor"
    SHELL_TYPE = "shellType"
    SHOTS = "shots"
    STUN_ICON = "stunIcon"
    TANK_LEVEL = "TankLevel"
    TANK_NAME = "tankName"
    TEMPLATE_MAIN_DMG = "templateMainDMG"
    TOTAL_DAMAGE = "totalDamage"
    USER_NAME = "userName"
    VEHICLE_CLASS = "vehicleClass"
    WARNING_MESSAGE = "incorrect event parameter for in damage log module {}"
    WG_ASSIST = "wg_log_hide_assist"
    WG_BLOCKED = "wg_log_hide_block"
    WG_CRITICS = "wg_log_hide_critics"
    WG_POS = "wg_log_pos_fix"
    NORMAL, GOLD = SHELL


ARCADE = namedtuple("ARCADE", (
    "NAME", "ANGLE", "DIST_RANGE", "MAX", "MIN", "START_ANGLE", "START_DEAD_DIST", "START_DIST", "SCROLL_SENSITIVITY"))(
    "arcade_camera", -0.20, "distRange", "max", "min", "startAngle", "startDeadDist", "startDist", "scrollSensitivity")

STRATEGIC = namedtuple("STRATEGIC", ("NAME", "MIN", "MAX", "DIST_RANGE", "SCROLL_SENSITIVITY"))(
    "strategic_camera", "min", "max", "distRange", "scrollSensitivity")
POSTMORTEM = namedtuple("POSTMORTEM", ("DURATION", "PARAMS", "CAM_MATRIX", "MODES"))(
    "transitionDuration", "postmortemParams", "camMatrix", {CTRL_MODE_NAME.POSTMORTEM, CTRL_MODE_NAME.DEATH_FREE_CAM})

__MESSAGES_TEMPLATE = {key: "<font size='20' color='#FAFAFA'>Change me in config. {}</font>".format(key) for key in
                       set(SHOT_RESULT_TO_ALT_COLOR.values() + SHOT_RESULT_TO_DEFAULT_COLOR.values())}

ARMOR_CALC = namedtuple("ARMOR_CALC", (
    "PIERCING_POWER", "NAME", "POSITION", "MESSAGES", "TEMPLATE", "MACROS_COLOR", "MACROS_COUNTED_ARMOR",
    "MACROS_PIERCING_RESERVE", "MACROS_MESSAGE", "MACROS_CALIBER", "RICOCHET", "NO_DAMAGE",
    "MESSAGES_TEMPLATE", "DEFAULT_TEMPLATE", "ON_ALLY"))(
    "piercingPower", "armor_calculator", "position", "messages", "template", "color", "countedArmor",
    "piercingReserve", "message", "caliber", "ricochet", "noDamage", __MESSAGES_TEMPLATE,
    "<p align='center'>%(ricochet)s%(noDamage)s\n<font color='%(color)s'>%(countedArmor)d</font></p>",
    "display_on_allies")

MARKERS = namedtuple("MARKERS", ("NAME", "HOT_KEY", "CLASS_COLOR", "TYPE_ICON", "ICON"))(
    "markers", "showMarkers_hotkey", "markersClassColor", {
        VEHICLE_CLASS_NAME.HEAVY_TANK: "H", VEHICLE_CLASS_NAME.MEDIUM_TANK: "M", VEHICLE_CLASS_NAME.AT_SPG: "J",
        VEHICLE_CLASS_NAME.SPG: "S", VEHICLE_CLASS_NAME.LIGHT_TANK: "L", "unknown": "U"}, "<font color='{}'>{}</font>")

CAROUSEL = namedtuple("CAROUSEL", ("NAME", "SMALL", "ROWS", "SETTINGS"))(
    "tank_carousel", "smallDoubleCarousel", "carouselRows", {GAME.CAROUSEL_TYPE: None, GAME.DOUBLE_CAROUSEL_TYPE: None})

FLIGHT_TIME = namedtuple("FLIGHT_TIME", ("NAME", "SPG_ONLY", "TEMPLATE", "M_FLIGHT_TIME", "M_DISTANCE", "ALIGN"))(
    "flight_time", "spgOnly", "template", "flightTime", "distance", "align")

VEHICLE_TYPES = namedtuple("VEHICLE_TYPES", ("NAME", "CLASS_COLORS", "CLASS_ICON", "UNKNOWN", "TEMPLATE"))(
    "vehicle_types", "vehicleClassColors", "vehicleClassIcon", "unknown",
    "<font face='BattleObserver' size='20'>{}</font>")

SIXTH_SENSE = namedtuple("SIXTH_SENSE", (
    "NAME", "PLAY_TICK_SOUND", "TIME", "DEFAULT", "ICON_NAME", "USER_ICON", "ICONS"))(
    "sixth_sense", "playTickSound", "lampShowTime", "default_icon", "default_icon_name", "user_icon",
    sixthSenseIconsNamesList()
)

__Dispersion = namedtuple("DISPERSION", (
    "NAME", "CIRCLE_EXTRA_LAP", "CIRCLE_SCALE_CONFIG", "CIRCLE_SERVER", "SCALE", "MAX_TIME", "SPG_GM_SCALE",
    "GUN_MARKER_MIN_SIZE", "MINUS_ONE_F", "CIRCLE_REPLACE"))
DISPERSION = __Dispersion(
    "dispersion_circle", "extraServerLap", "scale", "useServerAim", 0.70, 5.0, 0.8, 16.0, -1.0, "replaceOriginalCircle"
)

__DispersionTimer = namedtuple("dispersion_timer", ("NAME", "DONE_COLOR", "DONE_TEMPLATE", "REGULAR_TEMPLATE"))
DISPERSION_TIMER = __DispersionTimer("dispersion_timer", "done_color", "done_template", "regular_template")

DEBUG_PANEL = namedtuple("DEBUG_PANEL", (
    "NAME", "FPS_COLOR", "PING_COLOR", "LAG_COLOR", "STYLES", "STYLE"))(
    "debug_panel", "fpsColor", "pingColor", "pingLagColor", namedtuple("DebugStyles", ("minimal", "modern"))(
        "minimal", "modern"), "style")

BATTLE_TIMER = namedtuple("BATTLE_TIMER", (
    "NAME", "TEMPLATE", "COLOR", "END_COLOR", "M_TIMER", "TIME_FORMAT", "START_STRING", "END_BATTLE_SEC"))(
    "battle_timer", "timerTemplate", "timerColor", "timerColorEndBattle", "timer", "%02d:%02d", "00:00", 120)

EFFECTS = namedtuple("EFFECTS", (
    "NAME", "NO_FLASH_BANG", "NO_SHOCK_WAVE", "NO_BINOCULARS", "IS_PLAYER_VEHICLE", "SHOW_FLASH_BANG",
    "SHOW_SHOCK_WAVE", "NO_SNIPER_DYNAMIC"))(
    "effects", "noFlashBang", "noShockWave", "noBinoculars", "isPlayerVehicle", "showFlashBang", "showShockWave",
    "noSniperDynamic"
)

TEAM_BASES = namedtuple("TEAM_BASES", (
    "NAME", "TEXT_SETTINGS", "FONT", "SIZE", "BOLD", "ITALIC", "UNDERLINE", "BASE_FONT", "FONT_SIZE", "HUNDRED"))(
    "team_bases_panel", "text_settings", "font", "size", "bold", "italic", "underline", "$TitleFont", 16, 100.0)

BATTLE_ALIASES = namedtuple("BATTLE_ALIASES", (
    "MAIN_GUN", "HP_BARS", "DAMAGE_LOG", "DEBUG", "TIMER", "SIXTH_SENSE", "TEAM_BASES", "ARMOR_CALC",
    "FLIGHT_TIME", "DISPERSION_TIMER", "DATE_TIME", "DISTANCE", "OWN_HEALTH", "PANELS"))(
    "Observer_MainGun_UI", "Observer_TeamsHP_UI", "Observer_DamageLog_UI", "Observer_DebugPanel_UI",
    "Observer_BattleTimer_UI", "Observer_SixthSense_UI", "Observer_TeamBases_UI", "Observer_ArmorCalculator_UI",
    "Observer_FlightTime_UI", "Observer_DispersionTimer_UI", "Observer_DateTimes_UI", "Observer_Distance_UI",
    "Observer_OwnHealth_UI", "Observer_PlayersPanels_UI")

LOBBY_ALIASES = namedtuple("LOBBY_ALIASES", ("DATE_TIME", "AVG_DATA"))("Observer_DateTimes_UI", "Observer_AvgData_UI")

DISTANCE = namedtuple("DISTANCE", ("NAME", "TEMPLATE", "DIST", "TANK_NAME"))("distance_to_enemy", "template",
                                                                             "distance", "name")

OWN_HEALTH = namedtuple("OWN_HEALTH", ("NAME", "TEMPLATE"))("own_health", "template")

STATISTICS = namedtuple("STATISTICS", (
    "NAME", "STATISTIC_ENABLED", "CHANGE_VEHICLE_COLOR",
    "FULL_LEFT", "FULL_RIGHT",
    "CUT_LEFT", "CUT_RIGHT",
    "COLORS", "ICON_ENABLED", "ICON_BLACKOUT",
    "PANELS_FULL_WIDTH", "PANELS_CUT_WIDTH"))(
    "statistics", "statistics_enabled", "statistics_change_vehicle_name_color",
    "statistics_pattern_full_left", "statistics_pattern_full_right",
    "statistics_pattern_cut_left", "statistics_pattern_cut_right",
    "statistics_colors", "icon_enabled", "icon_blackout",
    "panels_full_width", "panels_cut_width"
)


class PANELS:
    def __init__(self):
        pass

    PANELS_NAME = "players_panels"
    # hp_bars
    BARS_ENABLED = "players_bars_enabled"
    BAR_SETTINGS = "players_bars_settings"
    BAR_TEXT_SETTINGS = "players_bars_text"
    BAR = "players_bars_bar"
    HP_TEMPLATE = "players_bars_hp_text"
    ON_KEY_DOWN = "players_bars_on_key_pressed"
    BAR_HOT_KEY = "players_bars_hotkey"
    BAR_CLASS_COLOR = "players_bars_classColor"
    # players_damages
    DAMAGES_ENABLED = "players_damages_enabled"
    DAMAGES_TEMPLATE = "players_damages_text"
    DAMAGES_SETTINGS = "players_damages_settings"
    DAMAGES_HOT_KEY = "players_damages_hotkey"
    DAMAGES_TF = "DamageTf"
    # another
    SPOTTED_FIX = "panels_spotted_fix"
    DAMAGE = "damage"


ANOTHER = namedtuple("ANOTHER", (
    "CONFIG_SELECT", "SHADOW_SETTINGS", "ACCOUNT_DBID", "USERS", "DBID", "BADGES", "IS_TEAM_KILLER",
    "NAME", "FAKE_NAME", "CLAN_DBID", "CLAN_ABBR"))(
    "configSelect", "shadow_settings", "accountDBID", "users", "databaseID", "badges", "isTeamKiller",
    "name", "fakeName", "clanDBID", "clanAbbrev")

CREW_XP = namedtuple("CREW_XP", (
    "NAME", "NOT_AVAILABLE", "IS_FULL_XP", "IS_FULL_COMPLETE", "NED_TURN_OFF", "ENABLE", "DISABLE"))(
    "crewDialog", "notAvailable", "isFullXp", "isFullComplete", "needTurnOff", "enable", "disable")

AVG_EFFICIENCY_HANGAR = namedtuple("AVG_EFFICIENCY_HANGAR", (
    "NAME", "ICONS", "DAMAGE", "ASSIST", "BLOCKED", "STUN", "MARKS_ON_GUN"
))("avg_efficiency_in_hangar", "icons", "avg_damage", "avg_assist", "avg_blocked", "avg_stun", "gun_marks")

# Settings Loader List
LOAD_LIST = (
    MAIN.NAME, HP_BARS.NAME, MAIN_GUN.NAME, DEBUG_PANEL.NAME, BATTLE_TIMER.NAME, DISPERSION.NAME, DISPERSION_TIMER.NAME,
    VEHICLE_TYPES.NAME, SNIPER.NAME, COLORS.NAME, ARMOR_CALC.NAME, TEAM_BASES.NAME, FLIGHT_TIME.NAME,
    SERVICE_CHANNEL.NAME, ARCADE.NAME, STRATEGIC.NAME, PANELS.PANELS_NAME, MINIMAP.NAME, EFFECTS.NAME,
    DAMAGE_LOG.WG_LOGS_FIX, DAMAGE_LOG.TOP_LOG, DAMAGE_LOG.EXTENDED, SIXTH_SENSE.NAME, ANOTHER.SHADOW_SETTINGS,
    CAROUSEL.NAME, CLOCK.NAME, DISTANCE.NAME, OWN_HEALTH.NAME, STATISTICS.NAME, AVG_EFFICIENCY_HANGAR.NAME
)


class CONFIG_INTERFACE:
    def __init__(self):
        pass

    DONATE_BUTTONS = ('donate_button_ua', 'donate_button_paypal', 'donate_button_patreon', 'discord_button')
    BLOCK_IDS = (
        ANOTHER.CONFIG_SELECT, MAIN.NAME, STATISTICS.NAME, DISPERSION.NAME, DISPERSION_TIMER.NAME, CAROUSEL.NAME,
        EFFECTS.NAME, DEBUG_PANEL.NAME, BATTLE_TIMER.NAME, CLOCK.NAME, HP_BARS.NAME, ARMOR_CALC.NAME,
        DAMAGE_LOG.WG_LOGS_FIX, DAMAGE_LOG.TOP_LOG, DAMAGE_LOG.EXTENDED, MAIN_GUN.NAME, TEAM_BASES.NAME,
        VEHICLE_TYPES.NAME, PANELS.PANELS_NAME, SNIPER.NAME, ARCADE.NAME, STRATEGIC.NAME, FLIGHT_TIME.NAME,
        MINIMAP.NAME, ANOTHER.SHADOW_SETTINGS, SIXTH_SENSE.NAME, DISTANCE.NAME, OWN_HEALTH.NAME, COLORS.NAME,
        SERVICE_CHANNEL.NAME, AVG_EFFICIENCY_HANGAR.NAME
    )
    HANDLER_VALUES = {
        SNIPER.NAME: {
            'dynamic_zoom*enabled': ('dynamic_zoom*steps_only',),
            'zoomSteps*enabled': ('zoomSteps*steps',),
            SNIPER.DISABLE_SNIPER: (SNIPER.SKIP_CLIP, SNIPER.DISABLE_LATENCY)
        },
        TEAM_BASES.NAME: {
            'outline*enabled': ('outline*color',)
        },
        PANELS.PANELS_NAME: {
            PANELS.BARS_ENABLED: (
                "players_bars_settings*players_bars_bar*outline*enabled",
                "players_bars_settings*players_bars_bar*outline*customColor",
                "players_bars_settings*players_bars_bar*outline*color",
                "players_bars_settings*players_bars_bar*outline*alpha",
                PANELS.BAR_HOT_KEY,
                PANELS.BAR_CLASS_COLOR,
                PANELS.ON_KEY_DOWN,
            ),
            PANELS.DAMAGES_ENABLED: (
                PANELS.DAMAGES_HOT_KEY, 'players_damages_settings*x', 'players_damages_settings*y'
            ),
        },
        HP_BARS.NAME: {
            'outline*enabled': ('outline*color',),
            'markers*enabled': ("markers*x", "markers*y", "markers*showMarkers_hotkey", "markers*markersClassColor")
        },
        MINIMAP.NAME: {
            'zoom*enabled': ('zoom*zoom_hotkey', 'zoom*indent'),
            MINIMAP.DEATH_PERMANENT: (MINIMAP.SHOW_NAMES,)
        },
        DEBUG_PANEL.NAME: {
            'debugGraphics*enabled': (
                'debugGraphics*pingBar*enabled', 'debugGraphics*fpsBar*enabled', 'debugGraphics*pingBar*color',
                'debugGraphics*fpsBar*color')
        },
        CLOCK.NAME: {
            'hangar*enabled': ('hangar*format', 'hangar*x', 'hangar*y'),
            'battle*enabled': ('battle*format', 'battle*x', 'battle*y')
        },
        SIXTH_SENSE.NAME: {
            SIXTH_SENSE.DEFAULT: (SIXTH_SENSE.ICON_NAME,)
        },
        STATISTICS.NAME: {
            STATISTICS.STATISTIC_ENABLED: (STATISTICS.PANELS_FULL_WIDTH, STATISTICS.PANELS_CUT_WIDTH,
                                           STATISTICS.CHANGE_VEHICLE_COLOR),
            STATISTICS.ICON_ENABLED: (STATISTICS.ICON_BLACKOUT,)
        }
    }


ALIAS_TO_CONFIG_NAME = {
    BATTLE_ALIASES.HP_BARS: HP_BARS.NAME,
    BATTLE_ALIASES.DAMAGE_LOG: DAMAGE_LOG.NAME,
    BATTLE_ALIASES.MAIN_GUN: MAIN_GUN.NAME,
    BATTLE_ALIASES.DEBUG: DEBUG_PANEL.NAME,
    BATTLE_ALIASES.TIMER: BATTLE_TIMER.NAME,
    BATTLE_ALIASES.SIXTH_SENSE: SIXTH_SENSE.NAME,
    BATTLE_ALIASES.TEAM_BASES: TEAM_BASES.NAME,
    BATTLE_ALIASES.ARMOR_CALC: ARMOR_CALC.NAME,
    BATTLE_ALIASES.FLIGHT_TIME: FLIGHT_TIME.NAME,
    BATTLE_ALIASES.DISPERSION_TIMER: DISPERSION_TIMER.NAME,
    BATTLE_ALIASES.PANELS: PANELS.PANELS_NAME,
    BATTLE_ALIASES.DATE_TIME: CLOCK.NAME,
    BATTLE_ALIASES.DISTANCE: DISTANCE.NAME,
    BATTLE_ALIASES.OWN_HEALTH: OWN_HEALTH.NAME
}
