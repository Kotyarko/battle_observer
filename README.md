### Официальные ресурсы
* [Тема обсуждения на форуме](http://forum.worldoftanks.ru/index.php?/topic/1385404-1500-battle-observer-1210-06052019/)
* [Канал на YouTube](https://www.youtube.com/channel/UCIksyJfDn5bOoig4iO7BKEA)
* [Сайт](http://armagomen.bb-t.ru/load/panel_scheta_team_hp/panel_scheta_ot_armagomen/9-1-0-1)

### Информация

#### Формат макроса:
```
%[(имя)][флаги][размер][.точность]тип (без квадратных скобок) - %(macrosName)s, %(macrosName).10s
```
#### Дополнительная информация по настройке макроса.
````
Для изменения формата чисел нужно редактировать только концовку и имя макроса, %(макрос)s 
заменить s на d - десятичное целое число, на .Nf - число с плавающей точкой где N(число) кол-во знаков после точки.
Все доступные макросы прописаны ниже.
ВАЖНО: чтобы написать знак % который будет выводится на экран и ничего не сломалось необходимо написать его дважды
Пример: %(percent)d%% вывод макроса будет результат_макроса%
````
#### Примеры форматирования числовых макросов:
```
к примеру у нас есть число 234.56789
%(макрос)s - выдаст число без изменений как дает питон. результат = 234.56789
s - применяется для всех макросов по умолчанию.
Если результатом макроса является НЕ число, значение менять НЕЛЬЗЯ.
В противном случае будет ошибка в питон логе и мод работать не будет.
Следующие примеры применимы только к числовым значениям.
%(макрос)d - результат = 234
%(макрос).1f - результат = 234.6
%(макрос).2f - результат = 234.57
```
#### Форматирование [html](https://help.adobe.com/ru_RU/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#htmlText)
#### Форматирование [даты и времени](https://docs.python.org/2/library/time.html#time.strftime)
```
Формат	Значение
%a	Сокращенное название дня недели
%A	Полное название дня недели
%b	Сокращенное название месяца
%B	Полное название месяца
%c	Дата и время
%d	День месяца [01,31]
%H	Час (24-часовой формат) [00,23]
%I	Час (12-часовой формат) [01,12]
%j	День года [001,366]
%m	Номер месяца [01,12]
%M	Число минут [00,59]
%p	До полудня или после (при 12-часовом формате)
%S	Число секунд [00,61]
%U	Номер недели в году (нулевая неделя начинается с воскресенья) [00,53]
%w	Номер дня недели [0(Sunday),6]
%W	Номер недели в году (нулевая неделя начинается с понедельника) [00,53]
%x	Дата
%X	Время
%y	Год без века [00,99]
%Y	Год с веком
%Z	Временная зона
%%	Знак '%'
```
#### user_background.json - позволяет добавлять на сцену статические пользовательские изображения.
**Важно: каждый отдельный фон должнен быть словарем c параметрами, от порядка добавления зависит слой наложения.**
````
"enabled":false,
"user_background": [
  {
   "smoothing":true, "x":0, "y":0, "alpha":0.9,
   "img":"mods/configs/mod_battle_observer/путь к изображению 1.png",
   "width":300,"height":150,
   "centeredX":false,"centeredY":false,"enabled":false
  },
  {
   "smoothing":true, "x":0, "y":0, "alpha":0.9,
   "img":"mods/configs/mod_battle_observer/путь к изображению 2.png",
   "width":300,"height":150,
   "centeredX":false,"centeredY":false,"enabled":false
  }
]

поля:
smoothing - Сглаживание.
alpha - прозрачность. от 0 до 1 (0.01 .... 1.00)
img - путь к изображению.
width ,height - Ширина, высота (изображения)
x, y - позиция на экране.
centeredX - true: начало координат по оси X - от центра экрана. false: от левого края экрана при положительных значениях X, и от правого при отрицательных
centeredY - true: начало координат по оси Y - от центра экрана. false: сверху экрана при положительных значениях Y, и от нижнего при отрицательных
enabled - выключатель изображения. true - показывать, false - скрыть
````
#### Макросы для расширенного лога полученного урона:
````
%(index)s          | порядковый номер.
%(shots)s          | Количество попаданий с уроном
%(totalDamage)s    | всего получено от танка противника / нанесено танку противника
%(lastDamage)s     | Последний выстрел
%(allDamages)s     | Список всех выстрелов через запятую 100, 23, 455, ..
%(classIcon)s      | иконка класса техники
%(tankName)s       | название танка
%(userName)s       | ник игрока
%(TankLevel)s      | уровень танка
%(tankClassColor)s | цвет класса техники
%(attackReason)s   | тип атаки.
%(iconName)s       | имя файла иконки танка.
%(killedIcon)s     | иконка уничтоженного / киллера(для лога входящего)
%(shellType)s      | Тип снаряда
%(shellIcon)s      | Тип снаряда (для изображений, поле определяет картинку с учотом голда/серебро параметр shellIcons)
%(shellColor)s     | Снаряды: золото / серебро
%(percentDamageAvgColor)s  | тип данных форматирования только s| Динамический цвет нанесенного урона по соотношению ненесено/полное хп вашего танка.
````
#### Макросы для расширенного лога нанесенного урона:
````
%(index)s          | порядковый номер.
%(shots)s          | Количество попаданий с уроном
%(totalDamage)s    | всего получено от танка противника / нанесено танку противника
%(lastDamage)s     | Последний выстрел
%(allDamages)s     | Список всех выстрелов через запятую 100, 23, 455, ..
%(classIcon)s      | иконка класса техники
%(tankName)s       | название танка
%(userName)s       | ник игрока
%(TankLevel)s      | уровень танка
%(tankClassColor)s | цвет класса техники
%(attackReason)s   | тип атаки.
%(iconName)s       | имя файла иконки танка.
%(killedIcon)s     | иконка уничтоженного / киллера(для лога входящего)
%(shellType)s      | Тип снаряда
%(shellIcon)s      | Тип снаряда (для изображений, поле определяет картинку с учотом голда/серебро параметр shellIcons)
%(percentDamageAvgColor)s  | тип данных форматирования только s| Динамический цвет нанесенного урона по соотношению ненесено/полное хп цели.
````
#### Макросы для ТОП лога:
````
%(tankDamageAvgColor)s | Динамический цвет урона в зависимости от нанесённого урона к среднему на текущем танке по вашему аккаунту
%(tankAvgDamage)s      | ваш средний урон на текущем танке
%(playerDamage)s       | Нанесённый лично
%(damageIcon)s         | Нанесённый лично иконка
%(blockedDamage)s      | Заблокированный бронёй
%(blockedIcon)s        | Заблокированный бронёй иконка
%(assistDamage)s       | Нанесённый с вашей помощью
%(assistIcon)s         | Нанесённый с вашей помощью иконка
%(spottedTanks)s       | Количество обнаруженных танков
%(spottedIcon)s        | Количество обнаруженных танков иконка
%(stunIcon)s           | Нанесённый по вашему оглушению иконка
%(stun)s               | Нанесённый по вашему оглушению
````
#### Макросы дебаг панели:
````
%(PING)s               | Пинг
%(FPS)s                | текущий фпс
%(pingColor)s          | цвет пинга/лагов настраивается в настройке цветов.
%(fpsColor)s           | цвет fps настраивается в настройке цветов.
````
#### Макросы таймера:
````
%(timer)s              | сам таймер.
%(timerColor)s         | цвет таймера (см настройку цветов)
````
#### Макросы мадали Основной калибр:
````
%(mainGunIcon)s        | Иконка основного калибра
%(mainGunDoneIcon)s    | зелёная иконка в виде птички(появляется только если условия выполнены)
%(mainGunFailureIcon)s | Иконка которая отображается если вас убили, либо оставшегося хп не хватает для получения медали.
%(mainGun)d            | Счетчик основного калибра
%(mainGunColor)s       | Цвет счётчика "основной калибр"
````
#### Хп игроков в ушах:
````
%(health)d             | Текущее ХП
%(maxHealth)d          | Максимальное ХП
%(percent).2f          | Текущий %
````
#### Урон игроков в ушах:
````
%(damage)s             | тип данных форматирования | выводит текущий урон если он больше 0
````
#### Калькулятор приведенной брони:
````
%(countedArmor)d       | приведённая броня.
%(piercingPower)d      | Пробитие снаряда с учётом расстояния.
%(piercingReserve)d    | Запас пробития.
%(caliber)d            | калибр снаряда.
%(color)s              | цвет (смотри настройку цветов)
%(ricochet)s           | Оповещение про возможный рикошет.
%(noDamage)s           | Оповещение о том что урона не будет. Снаряд попадет в модуль минуя основную броню. Гусеница без урона, колесо без урона и так далее.
%(message)             | Дополнительно сообщение из списка подставления По цвету.
````
#### Время полета снаряда:
````
%(flightTime).1f       | Время.
%(distance).1f         | Дистанция.
````
#### Лампочка (6е-чувство):
````
%(lampTime)d           | общее время лампы в секундах.
%(timeLeft)d           | остаток времени.
````
#### Макросы статистики WTR:
````
%(winRate).2f | процент побед (округление, смотри в примерах форматирования числовых макросов)
%(colorWTR)s  | цвет статистики
%(WTR)d       | статистика WTR
%(battles)s   | количество боев в формате 1K 1.23K 25.5K
%(nickname)s  | ник игрока
%(clanTag)s   | тэг клана ирока, если есть.
````