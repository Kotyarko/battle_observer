# coding=utf-8
from armagomen.battle_observer.core.bo_constants import MOD_VERSION

timeFormat_tooltip = """Формат - Значение
%a - Сокращенное название дня недели
%A - Полное название дня недели
%b - Сокращенное название месяца
%B - Полное название месяца
%c - Дата и время
%d - День месяца [01,31]
%H - Час (24-часовой формат) [00,23]
%I - Час (12-часовой формат) [01,12]
%j - День года [001,366]
%m - Номер месяца [01,12]
%M - Число минут [00,59]
%p - До полудня или после (при 12-часовом формате)
%S - Число секунд [00,61]
%U - Номер недели в году (нулевая неделя начинается с воскресенья) [00,53]
%w - Номер дня недели [0(Sunday),6]
%W - Номер недели в году (нулевая неделя начинается с понедельника) [00,53]
%x - Дата
%X - Время
%y - Год без века [00,99]
%Y - Год с веком
%Z - Временная зона
%% - Знак '%'"""
translate = {
    "configSelect": {
        "header": "ВЫБОР КОНФИГА",
        "selectedConfig": "Config",
        "donate_button_ua": "DONATE UA - Гривна",
        "donate_button_eu": "DONATE EUR|USD|RUB",
        "support_button": "Discord support"
    },
    "main": {
        "header": "Настройки без категории.",
        "enableBarsAnimation": "Включить анимацию всех панелей.",
        "showFriendsAndClanInEars": "Помечать друзей соклановцев и себя в списках команд.",
        "autoClearCache": "Очищать кэш игры после выхода.",
        "autoClearCache_tooltip": "Очистка временных файлов игры в папке AppData/Roaming/Wargaming.net/WorldOfTanks."
                                  "<br>Папки модификацый и настройки которые сохраняются там же, не затрагиваются.",
        "removeShadowInPrebattle": "Убрать затемнение таймера в начале боя",
        "hideBadges": "Отключить отображение нашивок",
        "hideBadges_tooltip": "в ушах, окне по tab, на экране загрузки.",
        "hideClanAbbrev": "Отключить отображение клана",
        "hideClanAbbrev_tooltip": "в ушах, окне по tab, на экране загрузки.",
        "fps_enableFPSLimiter": "Включить ограничитель FPS",
        "fps_enableFPSLimiter_tooltip": "НЕОБХОДИМ ПЕРЕЗАПУСК ИГРЫ ПОСЛЕ ПРИМЕНЕНИЯ НАСТРОЙКИ",
        "enableFPSLimiter_tooltip": "Внимание, для полного отключения или включения необходим перезапуск игры.",
        "fps_maxFrameRate": "Максимальный FPS",
        "hideChatInRandom": "Отключить чат в случайных боях",
        "hideChatInRandom_tooltip": "Полностью отключает чат в случайных боях.<br>Убирает форму чата и все "
                                    "что с ней связано.",
        "anonymousEnableShow": "Показывать анонимов.",
        "useKeyPairs": "Использовать парные Alt, Ctrl, Shift",
        "anonymousNameChange": "Изменить имена анонимов",
        "removeHandbrake": "Отключение ручного тормоза для ПТ-САУ",
        "hide_dog_tags": "Отключить отображение жетонов.",
        "ignore_commanders_voice": "Игнорировать озвучку командиров.",
        "ignore_commanders_voice_tooltip": "После включения будет принудительно использоваться стандартная озвучка"
                                           " экипажа. Параметр заменит все озвучки блогеров, Чака Норриса и так далее "
                                           "на стандартную/из мода озвучки."
    },
    "dispersion_circle": {
        "header": "Улучшенное сведение / серверный прицел.",
        "circle_enabled": "Улучшенный круг сведения.",
        "circle_extraServerLap": "Отображать как дополнительный серверный прицел.",
        "circle_extraServerLap_tooltip": "Добавит второй круг сведения серверного прицела.",
        "circle_replaceOriginalCircle": "Заменить оригинальный круг сведения уменшенным.",
        "circle_scale": "Множитель размера круга, 1 - 100 %",
        "circle_scale_tooltip": "Не рекомендуется выставлять значение ниже 65.",
        "timer_enabled": "Включить таймер сведения.",
        "timer_position_x": "Позиция таймера X",
        "timer_position_y": "Позиция таймера Y",
        "timer_color": "Цвет таймера еще не свелся.",
        "timer_done_color": "Цвет таймера/сообщения (полное сведение).",
        "timer_align": "Выравнивание текста."
    },
    "tank_carousel": {
        "header": "Настройка карусели танков.",
        "carouselRows": "Кол-во рядов многорядной карусели танков.",
        "carouselRows_tooltip": "Работает только если в клиенте включена многорядная карусель.",
        "smallDoubleCarousel": "Принудительно использовать маленькие иконки."
    },
    "effects": {
        "header": "Настройка визуальных эффектов.",
        "noShockWave": "Убрать тряску камеры при попадании по танку.",
        "noFlashBang": "Убрать красную вспышку при получении урона.",
        "noLightEffect": "Убрать вспышку и пламя после выстрела.",
        "noBinoculars": "Убрать затемнение в снайперском режиме"
    },
    "debug_panel": {
        "header": "Панель PING/FPS.",
        "debugText*text": "Тестовое поле для форматирования PING / FPS",
        "debugText*text_tooltip": "HTML - ДА<br>Макросы дебаг панели"
                                  "<br>%(PING)s | s:d:f | type data<tab>-Пинг"
                                  "<br>%(FPS)s | s:d:f | type data<tab>-текущий фпс"
                                  "<br>%(PingLagColor)s | s:d:f | type data"
                                  "<tab>-цвет пинг/лага настраивается в настройке цветов.",
        "debugText*x": "Позиция окна по оси X",
        "debugText*y": "Позиция окна по оси Y",
        "debugText*scale": "Масштабирование дебаг панели",
        "debugGraphics*enabled": "Показывать графические полосы пинг/фпс",
        "colors*fpsColor": "Цвет макроса %(fpsColor)s",
        "colors*pingColor": "Цвет макроса %(pingLagColor)s - Нет лагов",
        "colors*pingLagColor": "Цвет макроса %(pingLagColor)s - Есть лаги",
        "debugGraphics*fpsBar*color": "Цвет полосы FPS",
        "debugGraphics*fpsBar*enabled": "Включить графику для FPS",
        "debugGraphics*pingBar*color": "Цвет полосы PING",
        "debugGraphics*pingBar*enabled": "Включить графику для PING"
    },
    "battle_timer": {
        "header": "Таймер боя.",
        "timerTemplate": "Поле для форматирования таймера",
        "timerTemplate_tooltip": "Доступные макросы:<br> %(timer)s<br> %(timerColor)s<br>HTML - ДА",
        "timerColorEndBattle": "Цвет макроса %(timerColor)s менее 2 минут",
        "timerColor": "Цвет макроса %(timerColor)s нормальный"
    },
    "clock": {
        "header": "Панель Часов в бою\ангаре.",
        "battle*enabled": "Отображать в бою.",
        "hangar*enabled": "Отображать в ангаре.",
        "battle*format": "Форматирование строки.",
        "battle*format_tooltip": timeFormat_tooltip,
        "hangar*format": "Форматирование строки.",
        "hangar*format_tooltip": timeFormat_tooltip,
        "battle*x": "Позиция по горизонтали.",
        "battle*y": "Позиция по вертикали.",
        "hangar*x": "Позиция по горизонтали.",
        "hangar*y": "Позиция по вертикали."
    },
    "hp_bars": {
        "header": "Здоровье команд TeamHP.",
        "barsWidth": "Ширина полос",
        "differenceHP": "Показывать разницу между общим здоровьем команд",
        "showAliveCount": "Показывать на панели счета живых",
        "style": "Стиль панели",
        "outline*enabled": "Включить контур в стиле normal",
        "outline*color": "Цвет контура.",
        "markers*enabled": "Карусель маркеров техники.",
        "markers*x": "Расстояние по Горизонтали от центра.",
        "markers*x_tooltip": "Зеркально сдвигает значки от центра на заданное кол-во пикселей.",
        "markers*y": "Позиция по Вертикали от верха.",
        "markers*y_tooltip": "Позиция маркеров по Вертикали от верха экрана.",
        "markers*showMarkers_hotkey": "Клавиша включения/отключения маркеров.",
        "markers*markersClassColor": "Окрасить значки по цвету класса."
    },
    "armor_calculator": {
        "header": "Калькулятор приведенной брони.",
        "calcPosition*x": "Позиция текста по Горизонтали",
        "calcPosition*y": "Позиция текста по Вертикали",
        "showCalcPoints": "Показывать текст со значениями.",
        "template": "Шаблон строки со значениями.",
        "template_tooltip": "HTML - ДА<br>Макросы<br>%(calcedArmor)s | s:d:f | type data - приведённая броня."
                            "<br>%(armor)s | s:d:f | type data - броня без учёта наклона."
                            "<br>%(piercingPower)s | s:d:f | type data - Пробитие снаряда с учётом расстояния."
                            "<br>%(caliber)s | s:d:f | type data - калибр снаряда."
                            "<br>%(color)s | s:d:f | type data - цвет (смотри настройку цветов)"
    },
    "log_global": {
        "header": "Общие настройки логов.",
        "logsAltmode_hotkey": "Переключение логов в альтернативный режим",
        "wg_log_hide_assist": "Скрыть урон по разведданным",
        "wg_log_hide_assist_tooltip": "Убирает урон по разведданным из детального лога WG",
        "wg_log_hide_block": "Скрыть заблокированный урон",
        "wg_log_hide_block_tooltip": "Убирает заблокированный урон из детального лога WG",
        "wg_log_hide_crits": "Скрыть критические попадания",
        "wg_log_hide_crits_tooltip": "Убирает критические попадания из детального лога WG",
        "wg_log_pos_fix": "Поставить логи WG на правильные места.",
        "wg_log_pos_fix_tooltip": "Меняет местами логи полученного и нанесённого урона.<br>Полученный внизу, "
                                  "Нанесённый наверху."
    },
    "log_total": {
        "header": "СУММАРНЫЙ лог эффективности игрока.",
        "settings*inCenter": "Отображать лог в центре экрана",
        "settings*background": "Включить задний фон лога (отлько когда он в центре)",
        "settings*x": "Позиция основного лога по Горизонтали",
        "settings*y": "Позиция основного лога по Вертикали",
        "settings*align": "Выравнивание:",
        "settings*align_tooltip": "Выравнивание:<br>left - влево<br>center - по центру<br>right - вправо",
        "mainLogScale": "Масштабирование лога."
    },
    "log_damage_extended": {
        "header": "РАСШИРЕННЫЙ лог эффективности игрока.",
        "settings*x": "Позиция детального лога по Горизонтали.",
        "settings*x_tooltip": "Относительно левого списка игроков.",
        "settings*y": "Позиция детального лога по Вертикали.",
        "settings*y_tooltip": "Относительно левого списка игроков.",
        "settings*align": "Выравнивание:",
        "settings*align_tooltip": "Выравнивание:<br>left - влево<br>center - по центру<br>right - вправо",
        "reverse": "Развернуть лог.",
        "reverse_tooltip": "Добавлять новую строку на верх лога.",
        "shellColor*gold": "Цвет типа снарядов - Золото",
        "shellColor*normal": "Цвет типа снарядов - Серебро"
    },
    "log_input_extended": {
        "header": "РАСШИРЕННЫЙ лог полученного урона.",
        "settings*x": "Позиция детального лога по Горизонтали",
        "settings*x_tooltip": "Относительно дамаг панели.",
        "settings*y": "Позиция детального лога по Вертикали",
        "settings*y_tooltip": "Относительно дамаг панели.",
        "settings*align": "Выравнивание:",
        "settings*align_tooltip": "Выравнивание:<br>left - влево<br>center - по центру<br>right - вправо",
        "reverse": "Развернуть лог",
        "reverse_tooltip": "Добавлять новую строку на верх лога.",
        "shellColor*gold": "Цвет типа снарядов - Золото",
        "shellColor*normal": "Цвет типа снарядов - Серебро"
    },
    "main_gun": {
        "header": "Oсновной калибр.",
        "mainGunDoneIcon": "Настройка макроса - %(mainGunDoneIcon)s | s:d:f | type data",
        "mainGunDynamic": "Динамический расчёт урона до получения медали.",
        "mainGunFailureIcon": "Настройка макроса - %(mainGunFailureIcon)s | s:d:f | type data",
        "mainGunIcon": "Настройка макроса - %(mainGunIcon)s | s:d:f | type data",
        "settings*x": "Позиция по горизонтали (от центра экрана)",
        "settings*y": "Позиция по вертикали (от верхнего края)",
        "settings*align": "Выравнивание:",
        "settings*align_tooltip": "Выравнивание:<br>left - влево<br>center - по центру<br>right - вправо"
    },
    "team_bases_panel": {
        "header": "Индикация захвата базы.",
        "y": "Позиция полосы захвата по вертикали",
        "scale": "Масштабирование полос захвата.",
        "boBases": "Включить полосы захвата из мода.",
        "outline*enabled": "Включить контур.",
        "outline*color": "Цвет контура."
    },
    "vehicle_types": {
        "header": "Цвета классов техники.",
        "vehicleClassColors*AT-SPG": "Противотанковая САУ - ПТ-САУ",
        "vehicleClassColors*SPG": "Противотанковая САУ - Артиллерия",
        "vehicleClassColors*heavyTank": "Тяжёлый Танк",
        "vehicleClassColors*lightTank": "Лёгкий Танк",
        "vehicleClassColors*mediumTank": "Средний Танк",
        "vehicleClassColors*unknown": "Неизвестно (ГК)"
    },
    "players_panels": {
        "header": "Панели со списком игроков (уши).",
        "players_damages_enabled": "Урон игроков в списках команд.",
        "players_damages_hotkey": "Клавиша для отображения урона.",
        "players_damages_settings*x": "Положение текста по горизонтали",
        "players_damages_settings*y": "Положение текста по вертикали",
        "players_bars_enabled": "Хп игроков в ушах.",
        "players_bars_settings*players_bars_bar*outline*enabled": "Включить контур.",
        "players_bars_settings*players_bars_bar*outline*customColor": "Пользовательский цвет контура.",
        "players_bars_settings*players_bars_bar*outline*color": "Пользовательский цвет контура.",
        "players_bars_settings*players_bars_bar*outline*alpha": "Прозрачность контура.",
        "players_bars_hotkey": "Клавиша отображения ХП",
        "players_bars_classColor": "Окрасить полосы ХП в ушах по цвету типа техники.",
        "players_bars_on_key_pressed": "Отображать полосы только по нажатию клавиши.",
        "panels_icon_enabled": "Перекрасить иконки танков.",
        "panels_icon_enabled_tooltip": "Данная функция перекрашивает любые иконки техники в ушах в цвет классов"
                                       " техники.<br>Сила фильтра влияет на яркость."
                                       "<br>Рекомендуемая сила фильтра -1.25",
        "panels_icon_filter_strength": "Сила фильтра (яркость)",
        "panels_spotted_fix": "Исправить размер и позицию лампочек засвета."
    },
    "zoom": {
        "header": "Снайперский режим ZOOM-X.",
        "disable_cam_after_shoot": "Отключать снайперский режим после выстрела.",
        "disable_SniperCamera_After_Shoot_tooltip": "Автоматически переключает камеру в аркадный режим после выстрела"
                                                    " если калибр орудия больше 40мм.",
        "disable_cam_skip_clip": "Не выходить если магазинная система заряжания",
        "dynamic_zoom*enabled": "Автоматический выбор кратности Zoom.",
        "dynamic_zoom*enabled_tooltip": "Если данный параметр включён, <b>фиксированный Zoom</b> работать не будет.",
        "dynamic_zoom*zoomToGunMarker": "Включить приближение камеры к маркеру орудия",
        "dynamic_zoom*zoomToGunMarker_tooltip": "ВКЛЮЧЕНО: приближение к маркеру орудия.<br>ВЫКЛЮЧЕНО: без изменений."
                                                "<br><br>Простыми словами: куда дуло направлено туда и zoom / иначе "
                                                "куда камера.<br>Данный режим требует привыкания. Пример использования:"
                                                " наведите прицел в небо/на холм таким образом чтобы маркер орудия "
                                                "упёрся в препятствие(дом на пути) но при этом прицел был не на доме,"
                                                " перейдите в снайперский режим, получите Zoom на точку в которой было"
                                                " препятствие и увидите как работает данный параметр на практике.",
        "dynamic_zoom*zoomXMeters": "Чувствительность приближения в метрах.",
        "dynamic_zoom*zoomXMeters_tooltip": "(Автоматический выбор = расстояние/Чувствительность)<br>По умолчанию"
                                            " каждые 17 метров Zoom +1(чем меньше показатель тем больше Zoom)",
        "zoomSteps*enabled": "Заменить 'Шаги Zoom'.",
        "zoomSteps*steps": "Шаги Zoom.",
        "zoomSteps*steps_tooltip": "Можно записать любое кол-во через запятую и пробел либо просто запятую."
    },
    "arcade_camera": {
        "header": "Командирская камера (отдаление камеры).",
        "max": "Максимальное отдаление: по умолчанию 25.0",
        "min": "Максимальное приближение: по умолчанию 2.0",
        "startDeadDist": "Дистанция камеры при старте/уничтожении: по умолчанию 15"
    },
    "strategic_camera": {
        "header": "Артиллерийская камера (отдаление камеры).",
        "max": "Максимальное отдаление камеры: по умолчанию 100.0",
        "min": "Максимальное приближение камеры: по умолчанию 40.0"
    },
    "flight_time": {
        "header": "Время полета снаряда / Дистанция до цели.",
        "x": "Позиция текста по Горизонтали",
        "x_tooltip": "Положение от центра экрана. Выравнивание текста ---|центр|---",
        "y": "Позиция текста по Вертикали",
        "y_tooltip": "Положение от центра экрана.",
        "spgOnly": "Отображать время полёта только на арте.",
        "template": "Шаблон строки. Макросы: %(flightTime).1f , %(distance).1f",
        "wgDistDisable": "Скрыть базовую дистанцию в прицеле.",
        "align": "Выравнивание текста."
    },
    "save_shoot": {
        "header": "Блокировка выстрелов по союзникам и уничтоженным (save shoot lite).",
        "aliveOnly": "Заблокировать выстрел по уничтоженным.",
        "msg": "Сообщение о успешной блокировке, видно только вам.",
        "msg_tooltip": "Данное сообщение отображается только в случае блокировки выстрела по союзнику."
    },
    "minimap": {
        "header": "Мини-Карта.",
        "zoom*enabled": "Включить увеличение миникарты в центр.",
        "zoom*zoom_hotkey": "Клавиша для увеличения.",
        "zoom*indent": "Отступ от краёв экрана.",
        "zoom*indent_tooltip": "Необходимо указать отступ лишь от верхнего края.",
        "permanentMinimapDeath": "Всегда показывать уничтоженных на карте.",
        "showDeathNames": "Отображать имена уничтоженных танков."
    },
    "shadow_settings": {
        "header": "Настройка теней текста (свечения).",
        "inner": "Определяет, является ли свечение внутренним свечением.",
        "knockout": "Определяет, применяется ли к объекту эффект выбивки.",
        "blurX": "Степень размытия по горизонтали.",
        "blurY": "Степень размытия по вертикали.",
        "alpha": "Значение альфа-прозрачности цвета.",
        "color": "Цвет тени/свечения.",
        "strength": "Степень вдавливания или нанесения.",
        "blurY_tooltip": "Значения, являющиеся степенью 2 (т. е. 2, 4, 8, 16 и 32), оптимизируются и выполняются "
                         "быстрее, чем остальные.",
        "blurX_tooltip": "Значения, являющиеся степенью 2 (т. е. 2, 4, 8, 16 и 32), оптимизируются и выполняются "
                         "быстрее, чем остальные.",
        "inner_tooltip": "Значение 'Включено' говорит о том, что свечение внутреннее. "
                         "Значение 'Выключено' задает внешнее свечение (свечение вокруг внешнего контура объекта).",
        "knockout_tooltip": "Значение 'Включено' делает заливку объекта прозрачной и делает видимым цвет фона "
                            "документа. Значение по умолчанию — 'Выключено' (без эффекта выбивки).",
        "strength_tooltip": "Чем выше значение, тем более насыщен цвет тени и тем сильнее контраст между свечением и "
                            "фоном. Действительны значения от 0 до 255. По умолчанию — 2."
    },
    "colors": {
        "header": "Глобальные настройки цветов.",
        "armor_calculator*green": "Приведенная броня: Пробитие 100%",
        "armor_calculator*orange": "Приведенная броня: Пробитие 50%",
        "armor_calculator*red": "Приведенная броня: Пробитие 0%",
        "armor_calculator*yellow": "Приведенная броня: Пробитие 50% (Режим цветовой слепоты)",
        "armor_calculator*purple": "Приведенная броня: Пробитие 0% (Режим цветовой слепоты)",
        "main_gun*mainGunColor": "Основной калибр: Цвет макроса %(mainGunColor)s",
        "global*ally": "Голобальный цвет: союзники",
        "global*bgColor": "Цвет фона панелей",
        "global*enemyColorBlind": "Голобальный цвет: противник - цветовая слепота",
        "global*enemy": "Голобальный цвет: противник",
        "global*alpha": "Прозрачность панелей",
        "global*alpha_tooltip": "0 - прозрачно полностью.<br>1 - не прозрачно.",
        "global*bgAlpha": "Прозрачность фона панелей",
        "global*bgAlpha_tooltip": "0 - прозрачно полностью.<br>1 - не прозрачно.",
        "global*deadColor": "Голобальный цвет: уничтоженный",
    },
    "service_channel_filter": {
        "header": "Фильтр сообщений в системном канале - (скрывает сообщения выбранных категорий).",
        "sys_keys*CustomizationForCredits": "Кастомизация техники за кредиты.",
        "sys_keys*CustomizationForGold": "Кастомизация техники за золото.",
        "sys_keys*DismantlingForCredits": "Демонтаж оборудования за кредиты.",
        "sys_keys*DismantlingForCrystal": "Демонтаж оборудования за боны.",
        "sys_keys*DismantlingForGold": "Демонтаж оборудования за золото.",
        "sys_keys*GameGreeting": "Приветствие игры.",
        "sys_keys*Information": "Информационные сообщения.",
        "sys_keys*MultipleSelling": "Продажа, много предметов (со склада)",
        "sys_keys*PowerLevel": "Исследование модулей и техники",
        "sys_keys*PurchaseForCredits": "Покупки за кредиты.",
        "sys_keys*PurchaseForCrystal": "Покупки за боны.",
        "sys_keys*PurchaseForGold": "Покупки за золото.",
        "sys_keys*Remove": "Удаление предмета.",
        "sys_keys*Repair": "Ремонт (ручной режим)",
        "sys_keys*Restore": "Восстанвление",
        "sys_keys*Selling": "Продажа, один предмет.",
        "sys_keys*autoMaintenance": "Автоматическое обслуживание техники.",
        "sys_keys*customizationChanged": "Смена кастомизации"
    },
    "service": {
        "name": "Battle Observer - v{0}".format(MOD_VERSION),
        "description": "Открыть настройки мода Battle Observer",
        "windowTitle": "Настройки мода Battle Observer - v{0}".format(MOD_VERSION),
        "buttonOK": "OK",
        "buttonCancel": "Отмена",
        "buttonApply": "Применить",
        "enableButtonTooltip": "{HEADER}ВКЛ/ВЫКЛ{/HEADER}{BODY}Включить/Выключить модуль{/BODY}"
    },
    "updateDialog": {
        "buttonOK": "ПЕРЕЗАГРУЗКА",
        "buttonWAIT": "ПОДОЖДИТЕ",
        "titleWAIT": "Battle Observer Обновление - ПОДОЖДИТЕ",
        "titleOK": "Battle Observer Обновление - ГОТОВО",
        "messageWAIT": "Подождите, идет загрузка Обновления v{0}",
        "messageOK": "Нажмите ПЕРЕЗАГРУЗКА, для завершения процесса Обновления. v{0}",
        "buttonAUTO": "Автоматически",
        "buttonHANDLE": "Вручную",
        "messageNEW": "Доступна новая версия. v{0}\n\n"
                      "<b>Выберите вариант загрузки.</b>\n\n"
                      "<b>Автоматически</b> - загрузит и распакует архив обновления в папку. {1}\n\n"
                      "<b>Вручную</b> - откроет в браузере ссылку на этот-же архив но извлекать пакет и копировать "
                      "*.wotmod файл/ы прийдется в ручном режиме.\n",
        "titleNEW": "Доступна новая версия. v{0}"
    },
    "sixth_sense": {
        "header": "Лампа 6-е чувство.",
        "showTimer": "Отображать таймер.",
        "lampShowTime": "Длительность в секундах.",
        "playTickSound": "Воспроизводить звук таймера."
    }
}
