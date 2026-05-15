# Сметы MVP — варианты комплектующих AliExpress

Источник: [[Техническое задание]], [[Комплектующие MVP]], [[План разработки MVP]]

Дата подбора: 2026-05-15, цены AliExpress в EUR.

## Важные оговорки

- Цены на AliExpress быстро меняются и зависят от региона, доставки, купонов и выбранной вариации товара.
- AliExpress часто показывает минимальную цену по самой дешёвой вариации, поэтому перед покупкой обязательно открыть карточку и проверить выбранную комплектацию.
- Аккумуляторы на AliExpress — отдельный риск: доставка в РФ может быть ограничена, а качество и реальная ёмкость сильно различаются. Для первого полёта лучше дополнительно проверить локальные RC-магазины.
- В сметы не включены инструменты, паяльник, расходники, защита, кейс, доставка и возможная таможня.
- Цель этих смет — сравнить порядок стоимости и выбрать направление, а не финальный список покупки.

## Сортировка по общей стоимости

| Место | Вариант | Итого |
|---|---|---:|
| 1 | Ultra-budget S500 / Pixhawk 2.4.8 | €326.75 |
| 2 | Budget Holybro X500 + Matek | €652.43 |
| 3 | Balanced Holybro X500 + Pixhawk 6C Mini kit | €677.44 |
| 4 | High-quality original-TZ components | €1119.47 |

## Вариант 1 — Ultra-budget S500 / Pixhawk 2.4.8

Итого: **€326.75**

Смысл: самый дешёвый путь к летающему ArduPilot-MVP. Подходит для обучения, наземных тестов, настройки Mission Planner/QGroundControl и первых аккуратных полётов. Не стоит считать его хорошей платформой для будущего payload и wall-following.

| Узел | Вариант | Цена | Ссылка |
|---|---|---:|---|
| Рама + моторы + ESC | S500/X500/F450 frame + 2212 motors + 30A ESC kit | €61.99 | [AliExpress](https://fr.aliexpress.com/item/32914078336.html) |
| Flight controller + GPS + telemetry | Pixhawk 2.4.8 PRO + M8N GPS + 433/915 MHz telemetry + safety/buzzer | €73.99 | [AliExpress](https://fr.aliexpress.com/item/1005010114048408.html) |
| RC transmitter | FlySky FS-i6X + receiver | €39.39 | [AliExpress](https://fr.aliexpress.com/item/1005006860791905.html) |
| Аккумулятор | 6S LiPo/Li-ion candidate | €70.39 | [AliExpress](https://fr.aliexpress.com/item/1005010182981681.html) |
| Зарядка | ISDT 608AC / Genic Go charger | €50.99 | [AliExpress](https://fr.aliexpress.com/item/1005007512739386.html) |
| Мелочёвка | разъёмы, ремни, запасные пропеллеры, демпферы | €30.00 | оценка |

### Плюсы

- Минимальная цена входа.
- В комплекте Pixhawk обычно уже есть GPS, телеметрия, safety switch, buzzer.
- Не жалко использовать как учебную платформу.

### Минусы

- Pixhawk 2.4.8 — старый контроллер, не лучший выбор для долгого проекта.
- 2212-моторы и дешёвые ESC не дают серьёзного запаса под payload.
- Это скорее учебный коптер, а не основа будущего коптера-художника.
- Качество комплектов на AliExpress может плавать.

### Вывод

Брать только если цель — максимально дешёвое обучение ArduPilot и первые полёты. Для основного проекта лучше смотреть следующие варианты.

---

## Вариант 2 — Budget Holybro X500 + Matek

Итого: **€652.43**

Смысл: уже использовать нормальную X500-платформу, но не брать дорогой Pixhawk-комплект. Flight controller — Matek H743-WING V3 из исходного ТЗ.

| Узел | Вариант | Цена | Ссылка |
|---|---|---:|---|
| Рама/силовой комплект | Holybro X500 V2 ARF / power kit | €169.39 | [AliExpress](https://fr.aliexpress.com/item/1005009959413193.html) |
| Flight controller | Matek H743-WING V3 | €98.99 | [AliExpress](https://fr.aliexpress.com/item/1005010695414665.html) |
| GPS/compass | Holybro M10 GPS/compass | €45.99 | [AliExpress](https://fr.aliexpress.com/item/1005008103403502.html) |
| Telemetry | 3DR/SiK telemetry 433/915 MHz | €59.39 | [AliExpress](https://fr.aliexpress.com/item/1005007677779411.html) |
| RC transmitter | RadioMaster Pocket ELRS | €57.69 | [AliExpress](https://fr.aliexpress.com/item/1005010600069069.html) |
| Receiver | ELRS PWM receiver / PWM bridge | €15.00 | поиск: [AliExpress](https://www.aliexpress.com/w/wholesale-ELRS-PWM-receiver.html) |
| Аккумулятор | 6S 8000–10000 mAh LiPo candidate | €114.99 | [AliExpress](https://fr.aliexpress.com/item/1005009613866700.html) |
| Зарядка | ISDT 608AC / Genic Go charger | €50.99 | [AliExpress](https://fr.aliexpress.com/item/1005007512739386.html) |
| Мелочёвка | разъёмы, ремни, запасные пропеллеры, крепёж | €40.00 | оценка |

### Плюсы

- Нормальная база X500 для дальнейшего развития.
- Современный STM32H7 flight controller.
- RadioMaster + ELRS перспективнее, чем FlySky.
- Близко к исходному ТЗ.

### Минусы

- Matek H743-WING V3 — WING/VTOL-ориентированный контроллер. Перед покупкой нужно отдельно проверить удобство именно для ArduPilot Copter: разъёмы, питание, mounting, motor outputs, документация.
- Нужно больше ручной интеграции, чем с готовым Pixhawk kit.
- Не все провода/разъёмы будут plug-and-play.

### Вывод

Хороший бюджетный вариант, если хочется собрать проект руками и контролировать архитектуру. Но надо заранее проверить Matek H743-WING V3 именно для multirotor.

---

## Вариант 3 — Balanced Holybro X500 + Pixhawk 6C Mini kit

Итого: **€677.44**

Смысл: немного дороже варианта с Matek, но потенциально проще и надёжнее за счёт более стандартного Pixhawk-комплекта.

| Узел | Вариант | Цена | Ссылка |
|---|---|---:|---|
| Рама/силовой комплект | Holybro X500 V2 ARF / power kit | €169.39 | [AliExpress](https://fr.aliexpress.com/item/1005009959413193.html) |
| Flight controller kit | Pixhawk 6C Mini kit + PM06 + GPS M10 | €169.99 | [AliExpress](https://fr.aliexpress.com/item/1005011644475281.html) |
| Telemetry | 3DR/SiK telemetry 433/915 MHz | €59.39 | [AliExpress](https://fr.aliexpress.com/item/1005007677779411.html) |
| RC transmitter | RadioMaster Pocket ELRS | €57.69 | [AliExpress](https://fr.aliexpress.com/item/1005010600069069.html) |
| Receiver | ELRS PWM receiver / PWM bridge | €15.00 | поиск: [AliExpress](https://www.aliexpress.com/w/wholesale-ELRS-PWM-receiver.html) |
| Аккумулятор | 6S 10000–12000 mAh battery candidate | €114.99 | [AliExpress](https://fr.aliexpress.com/item/1005009613866700.html) |
| Зарядка | ISDT 608AC / Genic Go charger | €50.99 | [AliExpress](https://fr.aliexpress.com/item/1005007512739386.html) |
| Мелочёвка | разъёмы, ремни, запасные пропеллеры, крепёж | €40.00 | оценка |

### Плюсы

- Самый сбалансированный вариант для реального MVP.
- Pixhawk 6C Mini kit обычно проще интегрировать с ArduPilot/PX4, чем Matek WING-контроллер.
- GPS и power module уже в составе одного набора.
- X500 остаётся хорошей базой для следующих этапов.

### Минусы

- Немного дороже варианта с Matek.
- Нужно проверить, что комплект действительно включает нужный GPS, PM06 и кабели.
- Нужно отдельно выбрать телеметрию и RC-систему.

### Вывод

**Предварительно лучший вариант для покупки MVP**: не самый дешёвый, но снижает риск несовместимости и лишней ручной доработки.

---

## Вариант 4 — High-quality original-TZ components

Итого: **€1119.47**

Смысл: максимально близко к исходному ТЗ: X500 + T-Motor MN3508 KV380 + Hobbywing XRotor Pro 40A + Matek H743-WING V3. Это качественнее, но резко дороже.

| Узел | Вариант | Цена | Ссылка |
|---|---|---:|---|
| Рама | Holybro X500 V2 frame kit | €194.69 | [AliExpress](https://fr.aliexpress.com/item/1005010572292324.html) |
| Моторы | T-Motor MN3508 KV380 ×4 | €317.56 | [AliExpress](https://fr.aliexpress.com/item/1005008275083827.html) |
| ESC | Hobbywing XRotor Pro 40A, 2 pcs ×2 | €79.18 | [AliExpress](https://fr.aliexpress.com/item/1005008135880603.html) |
| Пропеллеры | 15×5.5 carbon props | €35.00 | поиск: [AliExpress](https://www.aliexpress.com/w/wholesale-15x5.5-carbon-propeller.html) |
| Flight controller | Matek H743-WING V3 | €98.99 | [AliExpress](https://fr.aliexpress.com/item/1005010695414665.html) |
| GPS/compass | Holybro M10 GPS/compass | €45.99 | [AliExpress](https://fr.aliexpress.com/item/1005008103403502.html) |
| Telemetry | 3DR/SiK telemetry 433/915 MHz | €59.39 | [AliExpress](https://fr.aliexpress.com/item/1005007677779411.html) |
| RC transmitter | RadioMaster Pocket ELRS | €57.69 | [AliExpress](https://fr.aliexpress.com/item/1005010600069069.html) |
| Receiver | ELRS PWM receiver / PWM bridge | €15.00 | поиск: [AliExpress](https://www.aliexpress.com/w/wholesale-ELRS-PWM-receiver.html) |
| Аккумулятор | 6S 10000–12000 mAh battery candidate | €114.99 | [AliExpress](https://fr.aliexpress.com/item/1005009613866700.html) |
| Зарядка | ISDT 608AC / Genic Go charger | €50.99 | [AliExpress](https://fr.aliexpress.com/item/1005007512739386.html) |
| Мелочёвка | крепёж, провода, разъёмы, демпферы, запасные винты | €50.00 | оценка |

### Плюсы

- Качественная силовая часть.
- Больше доверия к моторам/ESC.
- Лучше подходит под будущий payload, чем дешёвые 2212-комплекты.
- Ближе к исходной инженерной задумке.

### Минусы

- Стоимость почти в 3.4 раза выше ultra-budget варианта.
- Для первого MVP может быть избыточно.
- Всё равно остаётся вопрос по Matek H743-WING V3 для multirotor.
- При ошибках сборки/настройки цена ошибки выше.

### Вывод

Имеет смысл, если бюджет не критичен и цель — сразу качественная платформа. Для первого шага я бы не начинал с этого варианта без дополнительного расчёта тяги, веса и времени hover.

---

## Дополнительные найденные варианты и ссылки

### Holybro X500

- Holybro X500 V2 ARF / power kit — €169.39: [AliExpress](https://fr.aliexpress.com/item/1005009959413193.html)
- Holybro X500 V2 frame kit — €194.69: [AliExpress](https://fr.aliexpress.com/item/1005010572292324.html)
- Holybro X500 V2 ARF + Pixhawk 6X/6C/M10N/433/915 MHz — €215.99 по выдаче, но нужно проверять выбранную вариацию: [AliExpress](https://fr.aliexpress.com/item/1005010259259745.html)

### Flight controllers

- Matek H743-WING V3 — €98.99: [AliExpress](https://fr.aliexpress.com/item/1005010695414665.html)
- Matek H743-WING V3 alternate listing — €106.99: [AliExpress](https://fr.aliexpress.com/item/1005010444485260.html)
- Pixhawk 2.4.8 PRO + GPS + telemetry — €73.99: [AliExpress](https://fr.aliexpress.com/item/1005010114048408.html)
- Pixhawk 6C Mini kit + PM06 + GPS M10 — €169.99: [AliExpress](https://fr.aliexpress.com/item/1005011644475281.html)

### GPS

- Holybro M10 GPS/compass — €45.99: [AliExpress](https://fr.aliexpress.com/item/1005008103403502.html)
- Quescan M10 GPS + compass — €8.39, дешёвый рискованный вариант: [AliExpress](https://fr.aliexpress.com/item/1005006795079708.html)

### Telemetry

- 3DR/SiK telemetry 433/915 MHz — €59.39: [AliExpress](https://fr.aliexpress.com/item/1005007677779411.html)
- Holybro SiK Telemetry Radio V3 — €90.39: [AliExpress](https://fr.aliexpress.com/item/1005010243189639.html)

### RC

- FlySky FS-i6X + receiver — €39.39: [AliExpress](https://fr.aliexpress.com/item/1005006860791905.html)
- RadioMaster Pocket ELRS — €57.69: [AliExpress](https://fr.aliexpress.com/item/1005010600069069.html)

### Power

- 6S battery candidate — €70.39: [AliExpress](https://fr.aliexpress.com/item/1005010182981681.html)
- 6S 8000–12000+ mAh battery candidate — €114.99: [AliExpress](https://fr.aliexpress.com/item/1005009613866700.html)
- Tattu G-Tech 6S 16000/22000 mAh candidate — €165.99: [AliExpress](https://fr.aliexpress.com/item/1005009808549246.html)
- ISDT 608AC / Genic Go charger — €50.99: [AliExpress](https://fr.aliexpress.com/item/1005007512739386.html)

## Рекомендация

Для проекта «коптер-художник» я бы рассматривал так:

1. **Если цель — просто научиться и не жалко платформу:** Ultra-budget S500 / Pixhawk 2.4.8.
2. **Если цель — реальный MVP проекта:** Balanced Holybro X500 + Pixhawk 6C Mini kit.
3. **Если хочется следовать исходному ТЗ и бюджет позволяет:** High-quality original-TZ components, но только после расчёта тяги и проверки совместимости Matek H743-WING V3.

Моя предварительная рекомендация: **вариант 3 — Balanced Holybro X500 + Pixhawk 6C Mini kit**. Он всего на €25 дороже варианта с Matek, но выглядит менее рискованным по интеграции.

## Что проверить перед покупкой

- Точная комплектация Holybro X500 V2 ARF: входят ли моторы, ESC, пропеллеры, power board/module.
- Что именно входит в Pixhawk 6C Mini kit: GPS, power module, кабели, safety switch, buzzer.
- Частоту телеметрии: 433 MHz или 915 MHz, и что допустимо/удобно использовать локально.
- Совместимость ELRS-приёмника с выбранным flight controller: SBUS/CRSF/PWM.
- Разъёмы аккумулятора: XT60/XT90/EC5 и совместимость с power module.
- Реальную массу батареи.
- Наличие запасных пропеллеров и крепежа.
- Возможность доставки аккумуляторов.
- Нужен ли отдельный блок питания для зарядки, если зарядник выбран без встроенного AC power supply.

## Следующий шаг

Сделать расчёт веса/тяги для двух кандидатов:

- Budget Holybro X500 + Matek;
- Balanced Holybro X500 + Pixhawk 6C Mini kit.

После расчёта выбрать батарею и подтвердить, что hover throttle будет в безопасной зоне, а время полёта достаточно для первых тестов.
