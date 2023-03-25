# coding=utf-8

timeFormat_tooltip = "\n".join((
    "Формат - Значення",
    "%a - Скорочена назва дня тижня",
    "%A - Повна назва дня тижня",
    "%b - Скорочена назва місяця",
    "%B - Повна назва місяця",
    "%c - Дата та час",
    "%d - День місяця [01,31]",
    "%H - Час (24-год. формат) [00,23]",
    "%I - Час (12-год. формат) [01,12]",
    "%j - День року [001,366]",
    "%m - Номер місяця [01,12]",
    "%M - Кількість хвилин [00,59]",
    "%p - До полудня або після (при 12-годинному форматі)",
    "%S - Кількість секунд [00,61]",
    "%U - Номер тижня в році (0 тиждень починається з неділі) [00,53]",
    "%w - Номер дня тижня [0(Sunday),6]",
    "%W - Номер тижня в році (0 тиждень починається з понеділка) [00,53]",
    "%x - Дата - у форматі системної локалі",
    "%X - Час - у форматі системної локалі",
    "%y - Рік без століття [00,99]",
    "%Y - Рік зі століттям",
    "%Z - Назва часового поясу (без символів, якщо часовий пояс не існує).",
    "%% - Знак '%'"
))

RESTART_TOOLTIP = "Для увімкнення/вимкнення необхідний перезапуск гри."

localization = {
    "configSelect": {
        "header": "Варіанти налаштувань",
        "selector": "Вибрати налаштування:",
        "donate_button_ua": "Підтримати розробку",
        "donate_button_paypal": "Підтримати через PayPal",
        "donate_button_patreon": "Підтримати через Patreon",
        "discord_button": "Discord сервер модифікації"
    },
    "main": {
        "header": "Налаштування без категорії",
        "DEBUG_MODE": "DEBUG_MODE",
        "anonymousEnableShow": "Позначити гравців з прихованим нікнеймом",
        "anonymousEnableShow_tooltip":
            "Працює лише у випадку, якщо статистика гравців вимкнена. Заміняє нік та відмічає як team-killer",
        "autoClearCache": "Видаляти кеш після виходу з гри",
        "autoClearCache_tooltip": "Очищення тимчасових файлів гри у папці: AppData/Roaming/Wargaming.net/WorldOfTanks."
                                  "Налаштування модифікацій, які зберігаються у тому ж місці, залишаться.",
        "auto_crew_training": "Автоматичне перемикання 'Пришвидшеного навчання екіпажу'",
        "auto_crew_training_tooltip": "Відстежує чи прокачана/доступна 'Польова модернізація' та вмикає або вимикає "
                                      "'Пришвидшене навчання екіпажу' в залежності від цього.",
        "auto_return_crew": "Автоматичне повернення екіпажу",
        "auto_return_crew_tooltip": "Якщо на вибраному танку відсутній екіпаж, але він в наявності та не в бою на "
                                    "іншому танку, то екіпаж буде повернено в танк автоматично.",
        "disable_score_sound": "Вимкнути звук при знищенні союзного чи ворожого танку",
        "disable_stun_sound": "Вимкнути звук оглушення від артилерії",
        "do_not_buy_directives_for_currency_automatically": "Заощаджувати бони та срібло на настановах",
        "do_not_buy_directives_for_currency_automatically_tooltip":
            "Запобігає автоматичному поповненню настанов за бони або срібло, якщо їх не залишилось на складі. "
            "Модифікація також увімкне галочку 'Автоматичне поповнення' у випадку, якщо їх запас є на складі.",
        "hideBadges": "Вимкнути відображення нашивок у бою",
        "hideBadges_tooltip": "Вимкнення відображення нашивок в (бою, вухах, вікні по Tab, екрані завантаження).",
        "hideClanAbbrev": "Вимкнути відображення клан тегу",
        "hideClanAbbrev_tooltip": "Вимкнення відображення клан тегу в (бою, вухах, вікні по Tab, екрані завантаження).",
        "hide_button_counters_on_top_panel": "Вимкнути лічильники та підказки на кнопках у шапці гаражу.",
        "hide_button_counters_on_top_panel_tooltip": RESTART_TOOLTIP,
        "hide_dog_tags": "Вимкнути відображення жетонів у бою",
        "hide_field_mail": "Вимкнути польову пошту",
        "hide_hint_panel": "Вимкнути підказки в бою",
        "hide_main_chat_in_hangar": "Вимкнути спільний чат у гаражі",
        "hide_main_chat_in_hangar_tooltip": RESTART_TOOLTIP,
        "ignore_commanders_voice": "Ігнорувати озвучку командирів",
        "ignore_commanders_voice_tooltip": "Після увімкнення буде примусово використовуватися стандартна озвучка "
                                           "екіпажу. Параметр замінить всі унікальні озвучки командирів на стандартну "
                                           "або зі встановленого мода на озвучку.",
        "premium_time": "Відображати таймер часу дії преміум-аккаунту",
        "premium_time_tooltip": "Увімкнення або вимкнення відбувається не миттєво! Потрібно зачекати до "
                                "1 хвилини або змінити вкладку гаражу",
        "showFriendsAndClanInEars": "Позначити друзів, гравців клану та себе у списках команд",
        "useKeyPairs": "Використовувати парні Ctrl, Alt і Shift",
        "useKeyPairs_tooltip": "Після увімкнення ліва та права клавіша будуть працювати як одна, незалежно від того "
                               "яку ви вибрали в налаштуваннях модуля.",
        "save_shot": "Блокувати стрілянину по союзниках та знищених.",
        "mute_team_base_sound": "Вимкнути сирену захоплення бази."
    },
    "statistics": {
        "header": "Налаштування статистики гравців та іконки танків",
        "statistics_enabled": "Увімкнути статистику гравців за рейтингом WTR",
        "statistics_change_vehicle_name_color": "Змінити колір назви танку у списках на колір статистики гравця",
        "statistics_enabled_tooltip": "Статистика буде відображатися на екрані завантаження, у вухах, у вікні по "
                                      "клавіші Tab. Для більш тонкого налаштування дивись файл statistics.json"
                                      "Доступні імена макросів: WTR, colorWTR, winRate, nickname, battles, clanTag",
        "icon_enabled": "Іконки: Перефарбувати у кольори класів техніки",
        "icon_enabled_tooltip": "Дана функція перефарбовує будь-які іконки техніки на екрані завантаження, у вухах, "
                                "у вікні по клавіші Tab в колір класів техніки. Сила фільтра впливає на яскравість."
                                "Рекомендована сила фільтра: -1.25",
        "icon_blackout": "Іконки: Сила фільтра (яскравість)",
        "panels_full_width": "Ширина поля імені гравця (великі вуха)",
        "panels_cut_width": "Ширина поля імені гравця (малі вуха)",
    },
    "dispersion_circle": {
        "header": "Налаштування кола зведення, серверного прицілу",
        "extraServerLap": "Увімкнути серверний приціл (додаткове коло)",
        "extraServerLap_tooltip": "Увімкнення функції створить додаткове коло зведення серверного прицілу.",
        "replaceOriginalCircle": "Замінити оригінальне коло зведення",
        "scale": "Множник розміру кола 30-100% (0.3-1.0)",
        "scale_tooltip": "Даний параметр впливає на те, яким буде додаткове коло зведення у підсумку. "
                         "Якщо значення становить 0.3 (30%), то коло буде мінімально можливим, "
                         "а при 1.0 (100%) - максимально, тобто без змін. "
                         "Не рекомендується встановлювати значення менше 65%.",
    },
    "dispersion_timer": {
        "header": "Налаштування таймеру зведення",
        "x": "Позиція по горизонталі",
        "y": "Позиція по вертикалі",
        "color": "Колір: Не зведено",
        "done_color": "Колір: Повністю зведено",
        "align": "Вирівнювання тексту"
    },
    "tank_carousel": {
        "header": "Налаштування каруселі танків",
        "carouselRows": "Кількість рядів каруселі танків",
        "carouselRows_tooltip": "Працює тільки якщо немає івента, що змінює стандартну карусель.",
        "smallDoubleCarousel": "Примусово використовувати маленькі іконки"
    },
    "effects": {
        "header": "Налаштування візуальних ефектів",
        "noShockWave": "Вимкнути вібрацію камери при влучанні по танку",
        "noFlashBang": "Прибрати спалах при отриманні пошкоджень",
        "noBinoculars": "Прибрати затемнення у режимі снайпера",
        "noSniperDynamic": "Вимкнути динамічну камеру в режимі снайпера"
    },
    "debug_panel": {
        "header": "Налаштування панелі FPS та PING",
        "fpsColor": "Колір показника FPS",
        "pingColor": "Колір показника PING",
        "pingLagColor": "Колір показника LAG - Лаги присутні",
        "style": "Стиль панелі",
    },
    "battle_timer": {
        "header": "Налаштування таймера бою",
        "timerTemplate": "Поле для форматування таймера",
        "timerTemplate_tooltip": "Доступні макроси:\n%(timer)s - Таймер\n%(timerColor)s - Колір таймеру.",
        "timerColorEndBattle": "Колір макроса %(timerColor)s: залишається менше 2 хв.",
        "timerColor": "Колір макроса %(timerColor)s: більше 2 хв."
    },
    "clock": {
        "header": "Налаштування годинника в гаражі та бою",
        "battle*enabled": "Годинник в бою",
        "battle*format": "Годинник в бою: форматування",
        "battle*format_tooltip": timeFormat_tooltip,
        "battle*x": "Годинник в бою: позиція по горизонталі",
        "battle*y": "Годинник в бою: позиція по вертикалі",
        "hangar*enabled": "Годинник в гаражі",
        "hangar*format": "Годинник в гаражі: форматування",
        "hangar*format_tooltip": timeFormat_tooltip,
        "hangar*x": "Годинник в гаражі: позиція по горизонталі",
        "hangar*y": "Годинник в гаражі: позиція по вертикалі"
    },
    "hp_bars": {
        "header": "Налаштування панелі міцності команд",
        "showAliveCount": "Змінити лічильник на кількість живих",
        "style": "Стиль панелі"
    },
    "armor_calculator": {
        "header": "Налаштування калькулятора наведеної броні",
        "position*x": "Позиція по горизонталі, від центру",
        "position*y": "Позиція по вертикалі, від центру",
        "template": "Поле для форматування",
        "display_on_allies": "Відображати на союзниках",
        "template_tooltip": "Формат макросів: %(ім'я)тип даних s:d:f.\n"
                            "s-рядок, d-десяткове число, f-число із плаваючою точкою\n\n"
                            "Список доступних макросів:\n"
                            "%(countedArmor)d - Наведена броня\n"
                            "%(piercingPower)d - Пробиття снаряду з урахуванням відстані\n"
                            "%(piercingReserve)d - Запас пробиття після проходження броні\n"
                            "%(caliber)d - Калібр снаряду\n"
                            "%(message)s - Повідомлення із розділу \"messages\" в конфігураційному файлі\n"
                            "%(ricochet)s - Повідомлення про можливий рикошет\n"
                            "%(noDamage)s - Повідомлення про те, що пошкодження не буде. Снаряд потрапить у модуль, "
                            "оминаючи основну броню. Гусениця без пошкоджень, колесо без пошкоджень і т.д.\n"
                            "%(color)s - колір (дивись налаштування в розділі кольорів)\n"
    },
    "wg_logs": {
        "header": "Налаштування історії подій WG",
        "wg_log_hide_assist": "Приховати пошкодження по розвідданим",
        "wg_log_hide_assist_tooltip": "Приховує пошкодження по розвідданим із детальної історії подій",
        "wg_log_hide_block": "Приховати заблоковане пошкодження",
        "wg_log_hide_block_tooltip": "Приховує заблоковане пошкодження із детальної історії подій",
        "wg_log_hide_critics": "Приховати критичні попадання",
        "wg_log_hide_critics_tooltip": "Приховує критичні попадання із детальної історії подій",
        "wg_log_pos_fix": "Поставити логи гри на правильні місця",
        "wg_log_pos_fix_tooltip": "Міняє місцями історію подій отриманого й нанесеного/отриманого пошкодження."
    },
    "log_total": {
        "header": "Налаштування сумарної ефективності гравця",
        "settings*inCenter": "Відображати лог у центрі екрану",
        "settings*x": "Позиція основного лога по горизонталі",
        "settings*y": "Позиція основного лога по вертикалі",
        "settings*align": "Вирівнювання тексту:",
        "settings*align_tooltip": "left - зліва\ncenter - по центру\nright - справа",
        "mainLogScale": "Масштабування лога"
    },
    "log_extended": {
        "header": "Налаштування історії докладної шкоди",
        "logsAltMode_hotkey": "Перемикання історії шкоди у додатковий режим",
        "settings*x": "Позиція детальної шкоди по горизонталі",
        "settings*x_tooltip": "Від місця WG лога.",
        "settings*y": "Позиція детальної шкоди по вертикалі",
        "settings*y_tooltip": "Від місця WG лога.",
        "settings*align": "Вирівнювання тексту:",
        "settings*align_tooltip": "left - зліва\ncenter - по центру\nright - справа",
        "reverse": "Додавати нові події на початок",
        "reverse_tooltip": "Додавати новий рядок на початок історії",
        "shellColor*gold": "Колір преміум снарядів",
        "shellColor*normal": "Колір звичайних снарядів",
        "top_enabled": "Детальна історія нанесеної шкоди",
        "bottom_enabled": "Детальна історія отриманої шкоди",
    },
    "main_gun": {
        "header": "Налаштування медалі Основний калібр",
        "x": "Позиція по горизонталі (від центру екрана)",
        "y": "Позиція по вертикалі (від верхнього краю)",
        "progress_bar": "Смуга прогресу"
    },
    "team_bases_panel": {
        "header": "Налаштування індикатора захоплення бази",
        "y": "Позиція смуги захоплення по вертикалі",
        "scale": "Масштабування полос захоплення",
        "boBases": "Увімкнути смуги захоплення з мода",
        "outline*enabled": "Увімкнути контур",
        "outline*color": "Колір контура"
    },
    "vehicle_types_colors": {
        "header": "Налаштування кольорів класів техніки",
        "AT-SPG": "ПТ-САУ (Протитанкові САУ)",
        "SPG": "САУ (Артилерія)",
        "heavyTank": "Важкий танк",
        "lightTank": "Легкий танк",
        "mediumTank": "Середній танк",
        "unknown": "Невідомо (Глобальна мапа)"
    },
    "players_panels": {
        "header": "Налаштування панелей зі списком гравців",
        "players_damages_enabled": "Завдана гравцями шкода",
        "players_damages_hotkey": "Клавіша для відображення завданої шкоди",
        "players_damages_settings*x": "Позиція тексту по горизонталі",
        "players_damages_settings*y": "Позиція тексту по вертикалі",
        "players_bars_enabled": "Відображати міцність машин",
        "players_bars_settings*players_bars_bar*outline*enabled": "Увімкнути контур",
        "players_bars_settings*players_bars_bar*outline*customColor": "Користувацький колір контуру",
        "players_bars_settings*players_bars_bar*outline*color": "Колір контуру",
        "players_bars_settings*players_bars_bar*outline*alpha": "Прозорість контуру",
        "players_bars_hotkey": "Клавіша відображення міцності",
        "players_bars_classColor": "Пофарбувати смуги міцності у вухах по кольору типу техніки",
        "players_bars_on_key_pressed": "Відображати смуги тільки по натисканню клавіші",
        "panels_spotted_fix": "Виправити розмір й позицію лампочок виявлення"
    },
    "zoom": {
        "header": "Налаштування режиму снайпера",
        "disable_cam_after_shot": "Вимикати режим снайпера після пострілу",
        "disable_cam_after_shot_tooltip": "Автоматично перемикає камеру в режим аркади після пострілу, "
                                          "якщо калібр гармати більше 60мм.",
        "disable_cam_after_shot_latency": "Затримка автоматичного вимкнення режиму снайпера",
        "disable_cam_after_shot_skip_clip": "Не виходити з режиму, якщо є касетна система зарядження",
        "dynamic_zoom*zoomXMeters_tooltip": "За замовчуванням на кожні 20 метрів приходиться х1 "
                                            "кратності наближення. Чим менше показник чутливості - "
                                            "тим більше кратність наближення в співвідношенні (дистанція до "
                                            "цілі/дистанція для збільшення кратності).",
        "dynamic_zoom*enabled": "Автоматичний механізм вибору кратності наближення",
        "dynamic_zoom*enabled_tooltip": "Якщо дана функція увімкнена, то <b>фіксований параметр</b> працювати не буде. "
                                        "Автоматичний механізм вибору означає, що відстань до цілі в метрах ділене на "
                                        "чутливість буде використовуватись для вибору кратності зуму.\n",
        "dynamic_zoom*steps_only": "Переміщатися тільки по фіксованим крокам",
        "zoomSteps*enabled": "Замінити кратності зуму",
        "zoomSteps*steps": "Кроки кратності зуму",
        "zoomSteps*steps_tooltip": "Кроки кратності зуму потрібно записати через кому та пробіл або лише кому. "
                                   "Підтримується будь-яка кількість кроків."
    },
    "arcade_camera": {
        "header": "Налаштування командирської камери",
        "max": "Максимальне віддалення (за замовчуванням - 25)",
        "min": "Максимальне наближення (за замовчуванням - 2)",
        "startDeadDist": "Дистанція камери під час старту/знищення (за замовчуванням - 15)",
        "scrollSensitivity": "Чутливість прокрутки (за замовчуванням - 4)"
    },
    "strategic_camera": {
        "header": "Налаштування камери артилериста",
        "max": "Максимальне віддалення (за замовчуванням - 100)",
        "min": "Максимальное наближення (за замовчуванням - 40)",
        "scrollSensitivity": "Чутливість прокрутки (за замовчуванням - 10)"
    },
    "flight_time": {
        "header": "Налаштування часу польоту снаряду та дистанції до цілі",
        "x": "Позиція тексту по горизонталі",
        "x_tooltip": "Положення від центру екрана.",
        "y": "Позиція тексту по вертикалі",
        "y_tooltip": "Положення від центру екрана.",
        "spgOnly": "Відображати час польоту тільки на артилерії",
        "template": "Шаблон строки. Макроси: %(flightTime).1f , %(distance).1f",
        "align": "Вирівнювання тексту"
    },
    "minimap": {
        "header": "Налаштування міні-мапи",
        "zoom": "Увімкнути збільшення міні-мапи в центр",
        "permanentMinimapDeath": "Відображати знищених на мапі",
        "showDeathNames": "Відображати назви знищених танків",
        "real_view_radius": "Прибрати обмеження кругу огляду більше 445м",
        "yaw_limits": "Відображати кути горизонтального наведення на всій техніці, де можливо",
        "zoom_hotkey": "Клавіша для збільшення мапи"
    },
    "colors": {
        "header": "Налаштування глобальних кольорів мода",
        "armor_calculator*green": "Наведена броня: Шанс пробиття 100%",
        "armor_calculator*orange": "Наведена броня: Шанс пробиття 50%",
        "armor_calculator*red": "Наведена броня: Шанс пробиття 0%",
        "armor_calculator*yellow": "Наведена броня: Шанс пробиття 50% (режим колірної сліпоти)",
        "armor_calculator*purple": "Наведена броня: Шанс пробиття 0% (режим колірної сліпоти)",
        "global*ally": "Глобальний колір, союзник",
        "global*bgColor": "Колір фона панелей",
        "global*enemyColorBlind": "Глобальний колір: супротивники (колірна сліпота)",
        "global*enemy": "Глобальний колір, супротивник",
        "global*alpha": "Прозорість панелей",
        "global*alpha_tooltip": "0 - прозорий.\n1 - не прозорий.",
        "global*bgAlpha": "Прозорість фона панелей",
        "global*bgAlpha_tooltip": "0 - прозорий.\n1 - не прозорий.",
        "global*deadColor": "Глобальний колір, знищено",
    },
    "service_channel_filter": {
        "header": "Налаштування фільтра повідомлень у системному каналі",
        "sys_keys*CustomizationForCredits": "Налаштування техніки за кредити",
        "sys_keys*CustomizationForGold": "Налаштування техніки за золото",
        "sys_keys*DismantlingForCredits": "Демонтаж обладнання за кредити",
        "sys_keys*DismantlingForCrystal": "Демонтаж обладнання за бони",
        "sys_keys*DismantlingForGold": "Демонтаж обладнання за золото",
        "sys_keys*GameGreeting": "Вітання",
        "sys_keys*Information": "Інформаційні повідомлення",
        "sys_keys*MultipleSelling": "Продаж кількох предметів",
        "sys_keys*PowerLevel": "Дослідження модулів і техніки",
        "sys_keys*PurchaseForCredits": "Покупки за кредити",
        "sys_keys*PurchaseForCrystal": "Покупки за бони",
        "sys_keys*PurchaseForGold": "Покупки за золото",
        "sys_keys*Remove": "Видалення предмету",
        "sys_keys*Repair": "Ремонт",
        "sys_keys*Restore": "Відновлення",
        "sys_keys*Selling": "Продажа одного предмету",
        "sys_keys*autoMaintenance": "Автоматичне обслуговування техніки",
        "sys_keys*customizationChanged": "Налаштування змінено"
    },
    "service": {
        "name": "Battle Observer - v{0}",
        "description": "Відкрити налаштування мода Battle Observer",
        "windowTitle": "Налаштування мода Battle Observer - v{0}",
        "buttonOK": "Гаразд",
        "buttonCancel": "Скасувати",
        "buttonApply": "Застосувати",
        "enableButtonTooltip": "{HEADER}ВКЛ/ВИКЛ{/HEADER}{BODY}Увімкнути/Вимкнути модуль{/BODY}"
    },
    "sixth_sense": {
        "header": "Налаштування лампи шостого відчуття",
        "default_icon": "Використовувати вбудоване зображення.",
        "default_icon_name": "Вибрати вбудоване зображення.",
        "default_icon_tooltip": "Буде використовуватись вбудоване в мод зображення замість користувацького.",
        "lampShowTime": "Тривалість в секундах",
        "lampShowTime_tooltip": "<b>Як довго видно виявлену ціль?</b>\nПісля того як промені видимості одного танку "
                                "перетнулись з оглядовими точками іншого, то перший танк буде залишатися видимим, "
                                "навіть якщо промені видимості більше не взаємодіють з оглядовими точками. Звичайний "
                                "час, протягом якого танк залишається видимим — 10 секунд, але цей час можна як "
                                "зменшити до 8, так і збільшити до 16-18 секунд в залежності від встановленого на "
                                "танк обладнання, навичок та умінь членів екіпажу, та настанов.",
        "playTickSound": "Програвати звук таймера"
    },
    "distance_to_enemy": {
        "header": "Налаштування відстані до найближчого виявленого ворога",
        "x": "Позиція тексту по горизонталі",
        "x_tooltip": "Положення від центру екрана",
        "y": "Позиція тексту по вертикалі",
        "y_tooltip": "Положення від центру екрана",
        "template": "Шаблон строки. Макроси: %(distance)s, %(name)s",
        "align": "Вирівнювання тексту"
    },
    "own_health": {
        "header": "Налаштування міцності техніки гравця",
        "x": "Позиція тексту по горизонталі",
        "x_tooltip": "Положення від центру екрана",
        "y": "Позиция тексту по вертикалі",
        "y_tooltip": "Положення від центру екрана",
        "template": "Шаблон строки. Макроси: %(cur_health)s, %(max_health)s, %(per_health)s",
        "align": "Вирівнювання тексту"
    },
    "crewDialog": {
        "enable": "\nУвімкнути пришвидшене навчання екіпажу?",
        "disable": "\nВимкнути пришвидшене навчання екіпажу?",
        "notAvailable": "Польова модернізація недоступна для даної техніки",
        "isFullXp": "Ви набрали необхідну кількість досвіду для повної прокачки польової модернізації",
        "isFullComplete": "Ви прокачали польову модернізацію до максимально можливого рівня",
        "needTurnOff": "У вас не прокачана польова модернізація.\nРекомендовано вимкнути пришвидшене навчання екіпажу."
    },
    "avg_efficiency_in_hangar": {
        "header": "Налаштування віджета статистики танка в гаражі",
        "x": "Позиція віджета по горизонталі",
        "y": "Позиция віджета по вертикалі",
        "avg_damage": "Показати середню завдану шкоду",
        "avg_assist": "Показати середню шкоду, завдану з вашою допомогою",
        "avg_blocked": "Показати середню заблоковану бронею шкоду",
        "avg_stun": "Показати середню шкоду цілям, екіпажі яких ви оглушили (САУ)",
        "gun_marks": "Показати відсоток відмітної позначки",
    }
}
