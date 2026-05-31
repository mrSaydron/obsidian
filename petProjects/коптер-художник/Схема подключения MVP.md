# Схема подключения MVP

Источник: [[Комплектующие MVP]], [[Выбор компонентов/Как выбирать Flight Controller для MVP|Как выбирать Flight Controller для MVP]], [[Выбор компонентов/Как выбирать управление и связь для MVP|Как выбирать управление и связь для MVP]], [[Выбор компонентов/Как выбирать ESC для MVP|Как выбирать ESC для MVP]], [[Выбор компонентов/Как выбирать аккумулятор для MVP|Как выбирать аккумулятор для MVP]]

Контроллер: `Pixhawk 6C Mini`.

Формат схемы: Mermaid. Он удобен для Obsidian, потому что диаграмма хранится прямо в Markdown и её легко менять по мере выбора компонентов.

## Общая схема


```mermaid
---

title: Схема подключения MVP (v2)

---

  

flowchart TD

%% Полетный контроллер

subgraph controller["Pixhawk 6C Mini"]

subgraph up

CAN1

CAN2

GPS1

TELEM1

TELEM2

POWER1

end

  

subgraph left

GPS2

USB

I2C

FMUDebug["FMU Debug"]

end

  

subgraph right

PPM["PPM/SBUS RC"]

DSM

FLASH["FLASH CARD"]

end

  

subgraph IO_OUT["I/O PWM OUT"]

IO1

IO2

IO3

IO4

IO5

IO6

IO7

IO8

end

  

subgraph FMU["FMU PWM OUT"]

FMU1

FMU2

FMU3

FMU4

FMU5

FMU6

end

end

  

%% GPS модуль

GPS_module["GPS + compass module\nиз Pixhawk kit"]

Safety["Safety switch / buzzer\nесли отдельный модуль"]

  

%% модуль питания

subgraph powerModule["PM06 V2-14S"]

direction TB

pm_BAT

pm_toFC

pm_M1

pm_M2

pm_M3

pm_M4

end

  

accumulator["DXF 6S Lipo 10000 мАч"]

  

%% Электронные регуляторы скорости

esc1["BLHeli_S ESC SPRING 30A"]

esc2["BLHeli_S ESC SPRING 30A"]

esc3["BLHeli_S ESC SPRING 30A"]

esc4["BLHeli_S ESC SPRING 30A"]

  

%% Моторы

motor1["Cosmicrc 4108"]

motor2["Cosmicrc 4108"]

motor3["Cosmicrc 4108"]

motor4["Cosmicrc 4108"]

  

%% Винты

propeller1["HSKRC 15*5.5"]

propeller2["HSKRC 15*5.5"]

propeller3["HSKRC 15*5.5"]

propeller4["HSKRC 15*5.5"]

  

%% Управление и телеметрия

Transmitter["RadioMaster Pocket ELRS"]

Receiver["ELRS receiver\nCRSF UART"]

TelemetryAir["Telemetry radio\nair module"]

TelemetryGround["Telemetry radio\nUSB ground module"]

Laptop["Ноутбук\nMission Planner / QGroundControl"]

  

%% Подключения

accumulator -->|"VBAT + GND"| pm_BAT

pm_toFC -->|"POWER1: 5V + voltage/current sense + GND"| POWER1

  

pm_M1 ---|"VBAT + GND"| esc1

pm_M2 ---|"VBAT + GND"| esc2

pm_M3 ---|"VBAT + GND"| esc3

pm_M4 ---|"VBAT + GND"| esc4

  

IO1 ---|"PWM signal + GND"| esc1

IO2 ---|"PWM signal + GND"| esc2

IO3 ---|"PWM signal + GND"| esc3

IO4 ---|"PWM signal + GND"| esc4

  

esc1 ---|"3 фазных провода"| motor1

esc2 ---|"3 фазных провода"| motor2

esc3 ---|"3 фазных провода"| motor3

esc4 ---|"3 фазных провода"| motor4

  

motor1 --- propeller1

motor2 --- propeller2

motor3 --- propeller3

motor4 --- propeller4

  

GPS_module -->|"GPS1: UART + I2C compass + 5V + GND"| GPS1

Safety -. "safety/buzzer lines, если не встроены в GPS" .-> GPS1

  

Transmitter -->|"ELRS radio link"| Receiver

Receiver -->|"CRSF: TX/RX + 5V + GND"| TELEM2

  

TelemetryAir -->|"MAVLink UART: TX/RX + 5V + GND"| TELEM1

TelemetryGround -->|"MAVLink radio link"| TelemetryAir

Laptop -->|"USB"| TelemetryGround

Laptop -. "USB для настройки на столе" .-> USB
```
## Подключения к Pixhawk 6C Mini

| Узел | Порт Pixhawk 6C Mini | Что подключается | Комментарий |
|---|---|---|---|
| Power module | `POWER1` | 5V питание контроллера, voltage/current sense, GND | Pixhawk не питать напрямую от 6S. Через power module также настраивается battery monitor в ArduPilot. |
| GPS + compass | `GPS1` | UART GPS + I2C compass + safety switch/buzzer, если модуль это поддерживает | У Pixhawk 6C Mini `GPS1` совмещает UART, I2C, safety switch LED и buzzer линии. |
| RC receiver ELRS/CRSF | `TELEM2` / UART5 | TX/RX, 5V, GND | Для CRSF/ELRS нужен настоящий UART. `RC IN` лучше не использовать для ELRS/CRSF. |
| Telemetry radio | `TELEM1` / UART7 | TX/RX, 5V, GND | Для SiK/3DR MAVLink telemetry. Если модуль использует CTS/RTS, подключить полный 6-pin кабель. |
| ESC 1-4 | `MAIN OUT 1-4` | signal + GND к ESC | Плюс питания ESC идёт от PDB/батареи, не от Pixhawk. Красный BEC-провод от ESC не использовать для питания Pixhawk. |
| USB | USB-C / USB port | Ноутбук | Для прошивки, первичной настройки и логов на столе. В полёте лучше использовать telemetry radio. |

## Силовая схема

```mermaid
flowchart LR
    Battery["6S battery"] --> MainSwitch["Разъём / выключатель / anti-spark"]
    MainSwitch --> PM["PM06 V2-14S / power module + PDB"]

    PM -->|"5V + voltage/current"| Pixhawk["Pixhawk POWER1"]

    PM -->|"VBAT + GND"| ESC1["ESC 1"]
    PM -->|"VBAT + GND"| ESC2["ESC 2"]
    PM -->|"VBAT + GND"| ESC3["ESC 3"]
    PM -->|"VBAT + GND"| ESC4["ESC 4"]

    Pixhawk -->|"PWM signal + GND"| ESC1
    Pixhawk -->|"PWM signal + GND"| ESC2
    Pixhawk -->|"PWM signal + GND"| ESC3
    Pixhawk -->|"PWM signal + GND"| ESC4
```

Правила:

- силовой ток моторов не должен идти через Pixhawk;
- Pixhawk питается через `POWER1` от power module;
- ESC питаются от PDB / распределения питания; если используется `PM06 V2-14S` с силовыми площадками, он выполняет роль power module и PDB;
- сигнальные земли Pixhawk и ESC должны иметь общий `GND`;
- если ESC с BEC, красный 5V-провод с ESC не использовать как питание Pixhawk;
- разъём батареи, power module и PDB должны быть совместимы по току.

## RC и телеметрия

```mermaid
flowchart TD
    Transmitter["RadioMaster Pocket ELRS"] -->|"ELRS link"| Receiver["ELRS receiver"]
    Receiver -->|"CRSF UART"| Pixhawk["Pixhawk 6C Mini TELEM2"]

    Laptop["Ноутбук"] -->|"USB"| GroundRadio["Telemetry ground radio"]
    GroundRadio -->|"MAVLink 433/915 MHz"| AirRadio["Telemetry air radio"]
    AirRadio -->|"UART MAVLink"| PixhawkTelem["Pixhawk 6C Mini TELEM1"]
```

Роли разные:

- `RC link` нужен для ручного управления, arm/disarm, flight modes и аварийного перехвата;
- `telemetry link` нужен для Mission Planner/QGroundControl, параметров, предупреждений, battery monitor, GPS position и waypoint missions.

## Рекомендуемое распределение портов

| Порт | Занять сейчас | Состояние |
|---|---|---|
| `POWER1` | power module | занят |
| `GPS1` | GPS/compass/safety/buzzer из Pixhawk kit | занят |
| `TELEM1` | telemetry radio | занят |
| `TELEM2` | ELRS CRSF receiver | занят |
| `MAIN OUT 1-4` | ESC motors 1-4 | занят |
| `MAIN OUT 5-8` | не используется | свободно |
| `AUX OUT / FMU PWM OUT` | не используется | свободно |
| `CAN1/CAN2` | не используется | свободно |
| `I2C` | не используется, если compass уже в GPS1 | свободно |
| `GPS2` | не используется | свободно |

## Motor outputs

Для quadcopter в ArduPilot нужно сверить:

- frame class;
- frame type;
- motor order;
- направление вращения каждого мотора;
- соответствие `MAIN OUT 1-4` моторам на раме;
- ориентацию винтов.

Перед первым запуском:

1. Проверить motor order в Mission Planner без пропеллеров.
2. Проверить направление вращения моторов без пропеллеров.
3. Поставить винты только после проверки arm/disarm, failsafe и реакции стабилизации.

## Что пока не фиксируем моделью

Пока в схеме указаны типы, а не модели:

- аккумулятор;
- power module / current sensor, если он не будет точно из Pixhawk kit;
- PDB / распределение питания;
- GPS/compass, если комплект Pixhawk 6C Mini будет другой;
- telemetry radio;
- ELRS receiver;

## Важные замечания по Pixhawk 6C Mini

- В отличие от полноразмерного Pixhawk 6C, у Mini нет `POWER2` и `TELEM3`.
- Все основные разъёмы у Holybro указаны как JST-GH 1.25 mm, кроме специальных портов вроде debug/DSM.
- `POWER1` принимает 5V от power module и линии измерения тока/напряжения.
- `TELEM1` использует UART7, `TELEM2` использует UART5.
- `GPS1` включает UART1, I2C, safety switch, safety LED, buzzer и GND.
- Для CRSF/ELRS ArduPilot требует настоящий UART, поэтому использовать `TELEM2` разумнее, чем `RC IN`.

## Источники

- Holybro Pixhawk 6C Mini Ports: https://docs.holybro.com/autopilot/pixhawk-6c-mini/pixhawk-6c-mini-ports
- Holybro Pixhawk 6C Mini Difference: https://docs.holybro.com/autopilot/pixhawk-6c-mini/pixhawk-6c-mini-difference
- Holybro Pixhawk 6C Mini System Diagram & Pinout: https://docs.holybro.com/autopilot/pixhawk-6c-mini/system-diagram-and-pinout
- ArduPilot Pixhawk 6C / 6C Mini documentation: https://ardupilot.org/plane/docs/common-holybro-pixhawk6C.html
