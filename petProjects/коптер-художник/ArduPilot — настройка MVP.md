# ArduPilot — настройка MVP

Источник: [[Комплектующие MVP]], [[Схема подключения MVP]], [[Выбор компонентов/Как выбирать Firmware для MVP|Как выбирать Firmware для MVP]]

Цель документа: подготовить понятный порядок настройки `ArduPilot Copter` для MVP на `Pixhawk 6C Mini`.

## Текущая схема MVP

| Узел | Выбор / тип | Подключение |
|---|---|---|
| Flight controller | `Pixhawk 6C Mini` | USB для настройки, `POWER1` для питания |
| Firmware | `ArduPilot Copter` | прошивается через Mission Planner / QGroundControl |
| GPS + compass | модуль из Pixhawk kit | `GPS1` |
| RC receiver | `ELRS receiver`, `CRSF UART` | `TELEM2` |
| Telemetry radio | SiK/3DR telemetry radio | `TELEM1` |
| Power module | из Pixhawk kit / `PM06 V2-14S`, если подтвердится | `POWER1` |
| ESC | 4 отдельных ESC | `MAIN OUT 1-4` |
| Моторы | 4 мотора | через ESC |
| Аккумулятор | `6S 10000-12000 mAh` | через power module / PDB |

## Что можно сделать до прихода комплектующих

- установить Mission Planner или QGroundControl;
- прочитать базовую документацию ArduPilot Copter;
- сохранить ссылки на документацию Pixhawk 6C Mini;
- подготовить список параметров, которые нужно будет настроить;
- подготовить чеклист проверок без пропеллеров;
- выбрать открытое безопасное место для первого теста.

Фактическую прошивку, калибровки и motor test делать только с реальным контроллером и подключёнными модулями.

## Этап 1 — установка ПО на ноутбук

Основной вариант для ArduPilot: `Mission Planner`.

Что сделать:

1. Установить Mission Planner.
2. Проверить, что ноутбук видит USB-устройства.
3. Подготовить нормальный USB-кабель для Pixhawk.
4. Скачать документацию:
   - [[Даташиты/Pixhawk 6C Mini kit/README|Pixhawk 6C Mini kit — даташиты и документация]]
   - https://ardupilot.org/copter/
   - https://ardupilot.org/copter/docs/initial-setup.html

## Этап 2 — прошивка Pixhawk

Делать после получения контроллера.

Порядок:

1. Снять пропеллеры, если они уже установлены.
2. Подключить `Pixhawk 6C Mini` к ноутбуку по USB.
3. В Mission Planner открыть раздел установки firmware.
4. Выбрать `ArduPilot Copter`.
5. Выбрать target для `Pixhawk 6C Mini` / Holybro Pixhawk 6C Mini.
6. Дождаться окончания прошивки.
7. Переподключить Pixhawk.
8. Проверить, что Mission Planner подключается к контроллеру.

Важно: не выбирать прошивку для Plane/Rover/Sub. Нужен именно `Copter`.

## Этап 3 — базовая конфигурация рамы

Для нашего MVP:

| Параметр | Значение |
|---|---|
| Frame Class | `Quad` |
| Frame Type | `X` |
| Motor outputs | `MAIN OUT 1-4` |

Что проверить:

- стрелка на Pixhawk направлена вперёд по раме;
- если контроллер установлен иначе, настроить orientation в ArduPilot;
- рама физически соответствует `Quad X`;
- motor order соответствует схеме ArduPilot.

## Этап 4 — калибровка датчиков

Порядок:

1. Accelerometer calibration.
2. Compass calibration.
3. Проверка horizon / artificial horizon в Mission Planner.
4. Проверка барометра.
5. Проверка GPS lock на улице.

Компас калибровать после установки GPS/compass на реальное место на раме. Если компас находится рядом с силовыми проводами, показания могут быть плохими.

## Этап 5 — настройка портов

Предварительное распределение:

| Порт Pixhawk | Узел | Что настроить |
|---|---|---|
| `GPS1` | GPS + compass | GPS type, compass |
| `TELEM1` | telemetry radio | MAVLink telemetry |
| `TELEM2` | ELRS receiver | Serial protocol `CRSF` |
| `POWER1` | power module | voltage/current monitor |
| `MAIN OUT 1-4` | ESC | motor outputs |

Для `ELRS CRSF` важна логика TX/RX:

- TX приёмника идёт на RX порта Pixhawk;
- RX приёмника идёт на TX порта Pixhawk;
- питание приёмника: 5V + GND;
- не использовать `PPM/SBUS RC`, если приёмник работает по CRSF UART.

## Этап 6 — настройка радио

Что сделать:

1. Забиндить пульт RadioMaster Pocket ELRS и ELRS receiver.
2. Проверить, что приёмник получает питание от Pixhawk.
3. Настроить CRSF на `TELEM2`.
4. Выполнить radio calibration в Mission Planner.
5. Проверить каналы roll/pitch/throttle/yaw.
6. Назначить flight modes на переключатель.
7. Настроить arm/disarm.
8. Проверить RC failsafe.

Минимальные режимы:

- `Stabilize`;
- `AltHold`;
- `Loiter`, если GPS и compass работают стабильно;
- `RTL`.

## Этап 7 — настройка battery monitor

Power module подключается к `POWER1`.

Что настроить:

- тип battery monitor;
- voltage sensor;
- current sensor;
- ёмкость аккумулятора;
- предупреждение по низкому напряжению;
- failsafe по батарее.

Для 6S:

- полный заряд: около `25.2 V`;
- nominal: около `22.2 V`;
- пороги failsafe не задавать вслепую, сначала проверить рекомендации для выбранного аккумулятора.

## Этап 8 — ESC и моторы

До любых проверок моторы тестировать без пропеллеров.

Порядок:

1. Подключить ESC к `MAIN OUT 1-4`.
2. Проверить общий GND между Pixhawk и ESC.
3. Не питать Pixhawk от BEC ESC.
4. Выполнить ESC calibration, если она нужна для выбранных ESC.
5. Проверить motor order через Mission Planner Motor Test.
6. Проверить направление вращения каждого мотора.
7. При необходимости поменять любые две фазы мотора, чтобы изменить направление вращения.
8. Только после этого ставить пропеллеры правильной ориентации.

## Этап 9 — проверки без пропеллеров

Чеклист:

- Pixhawk прошит `ArduPilot Copter`;
- рама настроена как `Quad X`;
- accelerometer откалиброван;
- compass откалиброван;
- GPS видит спутники;
- радио откалибровано;
- flight modes переключаются;
- telemetry работает;
- battery voltage отображается правдоподобно;
- motor order правильный;
- motor direction правильный;
- failsafe при выключении пульта срабатывает ожидаемо;
- buzzer/safety switch работают, если есть в комплекте.

## Этап 10 — первый тестовый запуск

Перед первым включением с пропеллерами:

1. Проверить затяжку винтов рамы и моторов.
2. Проверить крепление аккумулятора.
3. Проверить центр масс.
4. Проверить ориентацию пропеллеров.
5. Проверить, что рядом нет людей и хрупких предметов.
6. Начинать с короткого hover на малой высоте.

После первого теста:

- проверить температуру моторов;
- проверить температуру ESC;
- проверить логи ArduPilot;
- проверить просадку батареи;
- проверить вибрации;
- записать результат в [[История]].

## Вопросы, которые нужно закрыть перед настройкой

- Какая точная комплектация `Pixhawk 6C Mini kit` пришла?
- Какой power module в комплекте: `PM02`, `PM06`, `PM07` или другой?
- Какой GPS/compass в комплекте?
- Есть ли safety switch и buzzer отдельными модулями?
- Какие ESC фактически куплены: 40A или 50A?
- Какой протокол ESC используем: PWM, DShot или другое?
- Какая батарея куплена: ёмкость, C-rate, разъём, масса?

