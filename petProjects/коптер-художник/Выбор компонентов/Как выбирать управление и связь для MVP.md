# Как выбирать управление и связь для MVP

Источник: [[Комплектующие MVP]], [[Выбор компонентов/Как выбирать Flight Controller для MVP|Как выбирать Flight Controller для MVP]], [[Выбор компонентов/Как выбирать Firmware для MVP|Как выбирать Firmware для MVP]], [[План разработки MVP]]

## Главный принцип

Управление коптером — это не только пульт.

Для MVP нужны минимум два канала:

- `RC control` — ручное управление, arm/disarm, выбор режимов, аварийное вмешательство;
- `telemetry` — связь с Mission Planner / QGroundControl для настройки, наблюдения, логов и миссий.

Практическая связка:

`пульт → RC receiver → Pixhawk → ArduPilot`

и отдельно:

`ноутбук / планшет → telemetry radio → Pixhawk → ArduPilot`

## Что должно быть в MVP

Минимально:

- RC transmitter;
- RC receiver;
- связь receiver с Pixhawk;
- настроенные flight modes;
- arm/disarm;
- RC failsafe;
- telemetry radio или другой канал MAVLink;
- Mission Planner или QGroundControl на ноутбуке;
- понятная процедура preflight-check.

Желательно:

- голосовые/звуковые предупреждения на пульте;
- отдельный switch для flight modes;
- отдельный switch для RTL/Land;
- RSSI/LQ telemetry от приёмника;
- battery voltage/current в наземной станции;
- geofence для первых тестов, если место позволяет.

## RC transmitter

Пульт нужен для ручного управления и аварийного перехвата.

Основные критерии:

- поддержка нужной радиосистемы: ELRS, FrSky, FlySky, Spektrum и т.д.;
- достаточное количество каналов;
- удобные стики;
- минимум 2-3 переключателя;
- настройка failsafe;
- возможность видеть RSSI/LQ;
- доступность приёмников.

Для ArduPilot желательно иметь каналы:

| Канал | Назначение |
|---|---|
| Roll | крен |
| Pitch | тангаж |
| Throttle | газ |
| Yaw | рыскание |
| Flight mode | Stabilize / AltHold / Loiter / Auto / RTL |
| Arm/disarm или safety action | опционально |
| RTL/Land | опционально, но полезно |

## RadioMaster Pocket ELRS

Статус: хороший текущий кандидат для MVP.

Плюсы:

- ELRS — современная и дальнобойная RC-система;
- хороший запас по качеству связи для MVP;
- компактный пульт;
- доступен на AliExpress;
- перспективнее старых бюджетных FlySky-комплектов.

Минусы:

- нужно отдельно выбрать подходящий receiver;
- ELRS требует настройки bind phrase / binding;
- нужно разобраться с каналами, model setup и failsafe;
- не все ELRS-приёмники одинаково удобно подключаются к Pixhawk.

## Receiver

Для Pixhawk/ArduPilot предпочтительно использовать serial receiver, а не PWM receiver.

### CRSF / ELRS по UART

Лучший вариант для RadioMaster Pocket ELRS.

Плюсы:

- один UART вместо множества PWM-проводов;
- низкая задержка;
- можно передавать качество связи;
- хорошо подходит для современных RC-систем.

Что проверить:

- есть ли у receiver выход CRSF;
- какой UART на Pixhawk будет использоваться;
- напряжение питания receiver: 5V или 3.3V;
- схема подключения TX/RX;
- поддержка в ArduPilot.

Важно: UART подключается перекрёстно:

- TX receiver → RX Pixhawk;
- RX receiver → TX Pixhawk;
- GND → GND;
- VCC → правильное питание.

### SBUS

Рабочий вариант, если receiver поддерживает SBUS.

Плюсы:

- распространённый serial-протокол;
- много инструкций.

Минусы:

- может требовать правильного входа/inverter;
- меньше информации о качестве связи, чем у CRSF/ELRS;
- не всегда самый удобный путь для ELRS.

### PWM receiver

Можно использовать, но для Pixhawk это менее удобно.

Минусы:

- много проводов;
- нужен PWM input / encoder или подходящий вход;
- хуже масштабируется;
- менее аккуратная сборка.

Для текущего MVP лучше целиться в `ELRS receiver с CRSF по UART`.

## Telemetry radio

RC-пульт управляет коптером, но для настройки и наблюдения нужна телеметрия.

Типовая схема:

`Pixhawk telemetry port → SiK/3DR telemetry radio → USB-модуль → ноутбук`

Что даёт telemetry:

- настройка ArduPilot без USB-кабеля;
- просмотр battery voltage/current;
- GPS position;
- flight mode;
- warnings;
- загрузка и запуск missions;
- базовый контроль состояния во время полёта.

Частые варианты:

- SiK/3DR telemetry 433 MHz;
- SiK/3DR telemetry 915 MHz;
- Wi-Fi telemetry для короткой дистанции;
- MAVLink через companion computer в будущем.

Что проверить:

- разрешённая/удобная частота в регионе;
- совместимость с Pixhawk telemetry port;
- разъёмы и кабели;
- мощность передатчика;
- антенны;
- дальность на реальной местности.

## Mission Planner и QGroundControl

Для ArduPilot обычно удобнее Mission Planner, особенно на Windows.

Mission Planner нужен для:

- прошивки;
- калибровки;
- настройки параметров;
- battery monitor;
- flight modes;
- failsafe;
- просмотра MAVLink telemetry;
- планирования waypoint missions;
- скачивания и анализа логов.

QGroundControl тоже можно использовать, особенно если привычнее PX4/QGC-экосистема. Для текущего MVP основной ориентир — Mission Planner, QGroundControl как альтернатива.

## Режимы полёта

Для первых тестов не нужно сразу начинать с Auto.

Практический набор:

| Режим | Для чего |
|---|---|
| Stabilize | базовая ручная стабилизация, требует управления газом |
| AltHold | удержание высоты, полезно после базовой проверки |
| Loiter | удержание позиции по GPS, после уверенного GPS/compass setup |
| RTL | возврат домой, нужен как аварийный режим |
| Land | автоматическая посадка |
| Auto | waypoint missions, только после базовых полётов |

На пульт стоит вывести минимум 3 режима:

- Stabilize;
- AltHold или Loiter;
- RTL.

Auto-миссии включать только после того, как ручные режимы, GPS, compass, battery failsafe и RTL уже проверены.

## Failsafe

Failsafe — обязательная часть управления.

Нужно настроить:

- RC loss failsafe;
- battery failsafe;
- GCS/telemetry loss, если используется;
- GPS failsafe / EKF failsafe;
- geofence, если подходит место испытаний.

Типовая логика для первых тестов:

- потеря RC → RTL или Land, в зависимости от места;
- низкая батарея → предупреждение, затем RTL/Land;
- критическая батарея → Land;
- плохой GPS → не использовать режимы, зависящие от GPS.

Важно: RTL безопасен только если корректно настроены home position, высота возврата, компас и GPS. В помещении или рядом со стенами RTL может быть опасен.

## Ручное управление vs автономность

Для проекта “коптер-художник” автономность будет нужна позже, но первый MVP должен уверенно управляться вручную.

Порядок развития:

1. Arm/disarm и проверка каналов без пропеллеров.
2. Первый ручной взлёт в Stabilize/AltHold.
3. Проверка Loiter на открытом месте.
4. Проверка RTL.
5. Простая waypoint mission.
6. Только потом эксперименты с удержанием у стены и будущим spray-control.

Не стоит начинать с waypoint missions, пока ручное управление и аварийные сценарии не проверены.

## Управление будущей системой распыления

На первом MVP реальную покраску не подключаем.

Но архитектурно нужно оставить возможность:

- отдельный PWM/relay output под макет клапана;
- канал на пульте для manual spray enable;
- MAVLink-команда от companion computer в будущем;
- failsafe, который выключает распыление при потере RC/GPS/аварии.

Главное правило: распыление не должно включаться только потому, что коптер включён. Нужен отдельный arm/enable logic.

## Предварительный выбор для MVP

Текущий ориентир:

- RC transmitter: `RadioMaster Pocket ELRS`;
- receiver: `ELRS receiver с CRSF UART`, не PWM-only;
- telemetry: `SiK/3DR telemetry radio 433/915 MHz` после проверки частоты и доставки;
- ground station: `Mission Planner`, QGroundControl как альтернатива;
- firmware: `ArduPilot Copter`;
- flight controller: `Pixhawk 6C Mini`.

## Чеклист перед покупкой

1. Пульт и receiver используют одну ELRS-частоту?
2. Receiver поддерживает CRSF по UART?
3. Есть ли свободный UART на Pixhawk для receiver?
4. Есть ли отдельный telemetry radio для Mission Planner?
5. Совместимы ли кабели с Pixhawk 6C Mini?
6. Сколько каналов нужно для flight modes и RTL?
7. Можно ли настроить RC failsafe?
8. Видны ли RSSI/LQ или другие показатели качества связи?
9. Разрешена/удобна ли частота telemetry: 433 или 915 MHz?
10. Есть ли понятная инструкция подключения к ArduPilot?

Для текущего MVP оптимально не смешивать задачи: RC-пульт отвечает за управление и аварийный перехват, telemetry отвечает за настройку, наблюдение и миссии.
