# Flight Controller — характеристики и ссылки

Источник: [[Комплектующие MVP]], [[Выбор компонентов/Как выбирать Flight Controller для MVP|Как выбирать Flight Controller для MVP]], [[Схема подключения MVP]]

## Сводная таблица

|   # | Контроллер                                  | Статус                              | Процессор     | Комплект                                                  |  Цена, р | Оценка                                                                      | Ссылка                                                                                                                                                                                                                               |
| --: | ------------------------------------------- | ----------------------------------- | ------------- | --------------------------------------------------------- | -------: | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Pixhawk 6C Mini kit + PM06 + GPS M10        | выбран                              | STM32H743     | FC, power module, GPS, кабели, состав проверить           |    16665 | лучший баланс интеграции для ArduPilot MVP                                  | https://www.ozon.ru/product/pixhawk-6c-mini-s-blokom-pitaniya-pm02-v3-12s-pm06-14s-i-gps-modulem-3897701193/?at=79tn0NE4NUNGOr64tYOmyXnSJjKRoYClyRL1DS6JP6mK&from_sku=3897702752&oos_search=false                                    |
|   2 | Matek H743-WING V3                          | запасной/не выбран                  | STM32H743     | только контроллер                                         |     6736 | мощный, но WING/VTOL-ориентирован и требует больше ручной интеграции        | [https://fr.aliexpress.com/item/1005010695414665.html](https://www.ozon.ru/product/poletnyy-kontroller-matek-h743-slim-v4-4220938788/?at=08tY9BM66cj72l43sxOG4YQH7p8VlyiZm8XE9fJog2qr)                                               |
|   3 | Pixhawk 2.4.8 PRO kit                       | учебный минимум                     | STM32F4-class | FC                                                        |     4655 | дешёвый учебный вариант, не лучший для долгого проекта                      | [https://fr.aliexpress.com/item/1005010114048408.html](https://www.ozon.ru/product/pixhawk2-4-8-px4-chetyrehosnyy-mnogoosevoy-3932044354/?at=pZtpJovXXhxE5XnlT1Wgyl0h587lXEcpgzrDkfW41px0)                                           |
|   4 | Pixhawk 2.4.8 с аксессуарами PPM/I2C/зуммер | учебный минимум / Ozon              | STM32F4-class | FC + PPM encoder + I2C splitter + buzzer, состав уточнить | уточнить | не заменяет Pixhawk 6C Mini kit: вероятно нет GPS, power module и telemetry | https://www.ozon.ru/product/kontroller-pixhawk-2-4-8-s-aksessuarami-ppm-i2c-zummerom-4277452240/                                                                                                                                     |
|   5 | Holybro Pixhawk 6C + PM07                   | CopterParts / альтернатива Mini     | STM32H743     | FC + PM07 power module, состав кабелей уточнить           |    34860 | современный Pixhawk, но не Mini; PM07 закрывает питание/PDB                 | https://copterparts.ru/product/%D0%BF%D0%BE%D0%BB%D0%B5%D1%82%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D0%BB%D0%B5%D1%80-holybro-pixhawk-6c-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C-%D0%BF%D0%B8%D1%82%D0%B0%D0%BD/ |
|   6 | Holybro Pixhawk 6C + GPS M9N + PM07         | CopterParts / альтернатива Mini kit | STM32H743     | FC + GPS M9N + PM07-12S + набор кабелей, состав проверить | уточнить | ближе всего к kit-логике, но это обычный 6C, а не 6C Mini                   | https://copterparts.ru/product/%D0%BF%D0%BE%D0%BB%D0%B5%D1%82%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D0%BB%D0%B5%D1%80-holybro-pixhawk-6c-gps/                                                                 |

## Что проверить

- точную комплектацию Pixhawk 6C Mini kit;
- входит ли power module и какой именно;
- входит ли GPS/compass и safety switch/buzzer;
- наличие кабелей JST-GH;
- поддержку ArduPilot Copter;
- свободные UART под ELRS receiver и telemetry.
- для Pixhawk 2.4.8 Ozon: есть ли GPS/compass, power module/current sensor и telemetry radio; по названию они не очевидны.

## Предварительный вывод

Для MVP оставляем `Pixhawk 6C Mini kit`, потому что он снижает риск несовместимости и даёт стандартную Pixhawk-экосистему.

## CopterParts

У CopterParts пока найден не `Pixhawk 6C Mini kit`, а обычный `Holybro Pixhawk 6C` в комплектах с `PM07` и, в одной карточке, с `GPS M9N`. Это технически близкая и даже более крупная Pixhawk-платформа, но она меняет выбранный контроллер и может потребовать другой монтаж.

Если покупать у CopterParts, нужно уточнить:

- есть ли именно `Pixhawk 6C Mini kit`;
- какая версия `PM07` входит в комплект;
- входит ли GPS/compass, safety switch, buzzer и все JST-GH кабели;
- совместим ли комплект с ArduPilot Copter из коробки.
