# GPS и компас — характеристики и ссылки

Источник: [[Комплектующие MVP]], [[Схема подключения MVP]], [[Сметы MVP — варианты комплектующих AliExpress]]

## Сводная таблица

| # | GPS / compass | Статус | GNSS | Компас | Цена | Оценка | Ссылка |
|---:|---|---|---|---|---:|---|---|
| 1 | GPS M10 из Pixhawk 6C Mini kit | основной кандидат | M10-class | проверить | входит в kit | предпочтительно использовать комплектный модуль | https://fr.aliexpress.com/item/1005011644475281.html |
| 2 | Holybro M10 GPS/compass | запасной/отдельная покупка | M10 | есть | €45.99 | нормальный вариант, если kit без GPS | https://fr.aliexpress.com/item/1005008103403502.html |
| 3 | Quescan M10 GPS + compass | дешёвый рискованный вариант | M10 | заявлен | €8.39 | только если бюджет критичен, качество проверить | https://fr.aliexpress.com/item/1005006795079708.html |
| 4 | Matek M9N-5883 GNSS & Compass | CopterParts / кандидат | u-blox M9N-class | QMC5883/compass по названию | 5700 р | хороший внешний GPS/compass, если kit без GPS; проверить кабель к Pixhawk GPS1 | https://copterparts.ru/product/gps-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C-matek-m9n-5883-gnss-compass/ |
| 5 | GPS M9N из Pixhawk 6C kit CopterParts | CopterParts / комплектный | M9N | проверить | входит в комплект | использовать, если берём Pixhawk 6C kit у CopterParts | https://copterparts.ru/product/%D0%BF%D0%BE%D0%BB%D0%B5%D1%82%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D0%BB%D0%B5%D1%80-holybro-pixhawk-6c-gps/ |

## Что проверить

- совместимость кабеля с `GPS1` Pixhawk 6C Mini;
- есть ли внешний компас;
- есть ли safety switch/buzzer в модуле или отдельно;
- длина кабеля и крепление на mast;
- отзывы по ArduPilot/Pixhawk.

## Предварительный вывод

Если `Pixhawk 6C Mini kit` включает GPS M10/compass, лучше начать с него. Отдельный Holybro M10 нужен, если комплектация kit окажется неполной.

## CopterParts

Если у выбранного `Pixhawk 6C Mini kit` GPS уже есть, отдельный GPS с CopterParts не нужен.

Если комплектация неполная, `Matek M9N-5883` выглядит нормальным отдельным вариантом. Главное перед покупкой — уточнить кабель/распиновку под Pixhawk `GPS1`, потому что у разных GPS-модулей могут отличаться разъёмы и порядок проводов.
