# CopterParts — подборка комплектующих

Источник проекта: [[Комплектующие MVP]], [[Детали и ссылки/Двигатели — таблица характеристик и цен]]

Дата поиска: 2026-05-22

Продавец:

https://copterparts.ru/

Важно: на карточках CopterParts часто указано, что перед заказом нужно связаться с продавцом для уточнения окончательной цены и наличия. Цены ниже — ориентир по карточкам/индексу на дату поиска.

## Краткий вывод

У CopterParts можно собрать заметную часть корзины для MVP, но не всё выглядит одинаково рационально.

Наиболее полезные позиции:

- моторы: `SunnySky X4108S KV380`, если покупаем моторы у CopterParts;
- ESC: `FATJAY 50A 2-6S` как простой кандидат или `Maytech MT50A-SBEC-FP32 50A` как более известный бренд;
- аккумулятор: `Z POWER LiPo 6S 10000mAh 22.2V XT60` как подходящий по ёмкости класс, но разъём `XT60` нужно проверить по току;
- GPS: `Matek M9N-5883 GNSS & Compass`, если GPS не входит в Pixhawk kit;
- управление: `RadioMaster Pocket M2 (ELRS)` + `RadioMaster RP4TD-M ELRS 2.4GHz` или другой CRSF-приёмник;
- зарядка: `SkyRC S100 Neo` как минимально разумная зарядка для 6S, `HTRC T240 DUO` или `SkyRC T400Q` удобнее, если батарей будет несколько.

Слабые места:

- `Pixhawk 6C Mini kit` у продавца пока не найден; есть обычный `Pixhawk 6C + GPS/PM07`;
- 15" пропеллеры есть, но цены высокие, особенно T-Motor;
- по PDB отдельно лучше ориентироваться на `PM07` из комплекта Pixhawk 6C или уточнять у продавца наличие отдельной PDB;
- многие карточки имеют маркетинговые описания, поэтому по силовым узлам обязательно сверять параметры с даташитом производителя.

## Сводная таблица

| Узел                        |                 Кандидат у CopterParts | Цена, р | Подходит?            | Комментарий                                                                                                               | Ссылка                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------- | -------------------------------------: | ------: | -------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Рама                        |                  Комплект Holybro X500 |   35000 | возможно             | Нужно уточнить, что входит: только рама или рама + силовая часть. Для 15" винтов X500 может быть на границе по габаритам. | https://copterparts.ru/product-category/%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C-%D1%80%D0%B0%D0%BC%D1%83-%D0%B4%D0%BB%D1%8F-%D0%BA%D0%B2%D0%B0%D0%B4%D1%80%D0%BE%D0%BA%D0%BE%D0%BF%D1%82%D0%B5%D1%80%D0%B0/holybro-%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C-%D1%80%D0%B0%D0%BC%D1%83-%D0%B4%D0%BB%D1%8F-%D0%BA%D0%B2%D0%B0%D0%B4%D1%80%D0%BE%D0%BA%D0%BE%D0%BF%D1%82%D0%B5%D1%80%D0%B0/ |
| Рама                        |                      Рама Holybro X650 |       - | хорошая альтернатива | 650 мм, 6S, заявлена поддержка 15" пропеллеров; может быть лучше X500, если точно идём в 15".                             | https://copterparts.ru/product/%D1%80%D0%B0%D0%BC%D0%B0-holybro-x650/                                                                                                                                                                                                                                                                                                            |
| Flight Controller           |    Holybro Pixhawk 6C + GPS M9N + PM07 |       - | возможно             | Это не Mini, но близкая современная Pixhawk-платформа. В комплекте заявлены GPS M9N и PM07-12S.                           | https://copterparts.ru/product/%D0%BF%D0%BE%D0%BB%D0%B5%D1%82%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D0%BB%D0%B5%D1%80-holybro-pixhawk-6c-gps/                                                                                                                                                                                                             |
| Flight Controller / питание |              Holybro Pixhawk 6C + PM07 |   34860 | возможно             | Обычный Pixhawk 6C, не Mini. PM07: 2S-14S, 90A, пик 140A, 8 пар ESC, XT60/AWG12.                                          | https://copterparts.ru/product/%D0%BF%D0%BE%D0%BB%D0%B5%D1%82%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D0%BB%D0%B5%D1%80-holybro-pixhawk-6c-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C-%D0%BF%D0%B8%D1%82%D0%B0%D0%BD/                                                                                                                                             |
| Мотор                       |                  SunnySky X4108S KV380 |    5000 | да                   | Лучший найденный мотор у продавца для 6S и 14-15". Подробнее в таблице двигателей.                                        | https://copterparts.ru/product/%D0%B4%D0%B2%D0%B8%D0%B3%D0%B0%D1%82%D0%B5%D0%BB%D1%8C-sunnysky-x4108s-kv380/                                                                                                                                                                                                                                                                     |
| Мотор                       | T-Motor MN4006 Antigravity 380KV, 2 шт |   19990 | да, но дорого        | Технически сильный вариант, цена примерно 9995 р за мотор.                                                                | https://copterparts.ru/product/%D0%B4%D0%B2%D0%B8%D0%B3%D0%B0%D1%82%D0%B5%D0%BB%D1%8C-t-motor-mn4006-antigravity-380kv-2%D1%88%D1%82/                                                                                                                                                                                                                                            |
| ESC                         |                        FATJAY 50A 2-6S |    5100 | возможно             | 50A continuous, 60A burst, 2-6S. Простой кандидат, но бренд/прошивку и работу с большими винтами нужно уточнить.          | https://copterparts.ru/product/esc-%D1%80%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80-fatjay-50a-2-6s/                                                                                                                                                                                                                                                                       |
| ESC                         |            Maytech MT50A-SBEC-FP32 50A |    4900 | возможно             | 50A, 2-6S, BLHeli_32, BEC. Для Pixhawk BEC не использовать как основное питание.                                          | https://copterparts.ru/product/esc-%D1%80%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80-maytech-mt50a-sbec-fp32-50a/                                                                                                                                                                                                                                                           |
| ESC                         |                           MAD AM32 50A |       - | под вопросом         | 50A, 2-6S, AM32, telemetry/DroneCAN заявлены. Может быть интересно, но для первого MVP усложняет настройку.               | https://copterparts.ru/product/esc-%D1%80%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80-mad-am32-50a/                                                                                                                                                                                                                                                                          |
| Аккумулятор                 |    Z POWER LiPo 6S 10000mAh 22.2V XT60 |   18450 | возможно             | Ёмкость подходит. Нужно уточнить C-rate, массу и не станет ли XT60 узким местом. Для нашей сборки спокойнее XT90.         | https://copterparts.ru/product/%D0%B0%D0%BA%D0%BA%D1%83%D0%BC%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80-z-power-lipo-6s-10000mah-22-2v-xt60/                                                                                                                                                                                                                                           |
| Аккумулятор                 |           Turnigy 10000mAh 6S 12C XT90 |       - | возможно             | Хороший формат разъёма XT90, но 12C надо проверить по реальному току и массе.                                             | https://copterparts.ru/product/%D0%B0%D0%BA%D0%BA%D1%83%D0%BC%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80-turnigy-%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%BE%D0%B9-%D0%B5%D0%BC%D0%BA%D0%BE%D1%81%D1%82%D0%B8-10000-%D0%BC%D0%B0%D1%87-6s-12c-lipo-pa/                                                                                                                                         |
| Пропеллеры                  |   T-Motor 14x4.8, комплект CW/CCW 2 шт |    9800 | подходит, но дорого  | Хорошая пара для T-Motor/SunnySky 380KV, но цена высокая для расходника.                                                  | https://copterparts.ru/product-category/%D0%BB%D0%BE%D0%BF%D0%B0%D1%81%D1%82%D0%B8-%D0%B8-%D0%BF%D1%80%D0%BE%D0%BF%D0%B5%D0%BB%D0%BB%D0%B5%D1%80%D1%8B/                                                                                                                                                                                                                          |
| Пропеллеры                  |  T-Motor P16x5.4, комплект CW/CCW 2 шт |   16500 | вероятно крупноват   | Для X500 может не влезть, для X650 проверить зазор. Дорого.                                                               | https://copterparts.ru/product-category/%D0%BB%D0%BE%D0%BF%D0%B0%D1%81%D1%82%D0%B8-%D0%B8-%D0%BF%D1%80%D0%BE%D0%BF%D0%B5%D0%BB%D0%BB%D0%B5%D1%80%D1%8B/                                                                                                                                                                                                                          |
| GPS/compass                 |          Matek M9N-5883 GNSS & Compass |    5700 | да                   | Подходит как внешний GNSS + compass, если не берём Pixhawk kit с GPS. Проверить разъём под Pixhawk.                       | https://copterparts.ru/product/gps-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C-matek-m9n-5883-gnss-compass/                                                                                                                                                                                                                                                                             |
| RC-пульт                    |             RadioMaster Pocket M2 ELRS |       - | да                   | Совпадает с нашим предварительным выбором по классу. Нужно уточнить частоту: 2.4GHz ELRS.                                 | https://copterparts.ru/product/%D0%B0%D0%BF%D0%BF%D0%B0%D1%80%D0%B0%D1%82%D1%83%D1%80%D0%B0-%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-radiomaster-pocket-m2-elrs/                                                                                                                                                                                             |
| RC receiver                 |        RadioMaster RP4TD-M ELRS 2.4GHz |    3500 | да                   | CRSF, 5V, ELRS V3.4.3. Хороший кандидат под Pixhawk UART.                                                                 | https://copterparts.ru/product/%D0%BF%D1%80%D0%B8%D1%91%D0%BC%D0%BD%D0%B8%D0%BA-radiomaster-rp4td-m-elrs-24-%D0%B3%D0%B3%D1%86/                                                                                                                                                                                                                                                  |
| RC receiver                 |            RadioMaster ER4 ELRS 2.4GHz |    3000 | возможно             | Серия ER обычно удобна для PWM/servo, для Pixhawk нужен CRSF/UART — уточнить перед покупкой.                              | https://copterparts.ru/product/%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%BD%D0%B8%D0%BA-radiomaster-er4-elrs-2-4%D0%B3%D0%B3%D1%86/                                                                                                                                                                                                                                                      |
| Зарядка                     |                         SkyRC S100 Neo |    5350 | минимально да        | 1-6S, AC 100W / DC 200W. Для 6S 10000mAh будет заряжать медленнее 1C от AC, но для старта годится.                        | https://copterparts.ru/product/%D0%B7%D0%B0%D1%80%D1%8F%D0%B4%D0%BD%D0%BE%D0%B5-%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%BE-skyrc-s100-neo/                                                                                                                                                                                                                     |
| Зарядка                     |                          HTRC T240 DUO |    9900 | да                   | 2 канала, до 10A, 150W, 1-6S. Удобнее, если будет 2 аккумулятора.                                                         | https://copterparts.ru/product/%D0%B7%D0%B0%D1%80%D1%8F%D0%B4%D0%BD%D0%BE%D0%B5-%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%BE-htrc-t240-duo/                                                                                                                                                                                                                      |
| Зарядка                     |                            SkyRC T400Q |   22710 | да, но дорого        | 4 канала по 100W, 1-6S. Хорошо для парка батарей, избыточно для первой одной батареи.                                     | https://copterparts.ru/product/%D0%B7%D0%B0%D1%80%D1%8F%D0%B4%D0%BD%D0%BE%D0%B5-%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%BE-skyrc-t400q/                                                                                                                                                                                                                        |

## Предварительная корзина у CopterParts

Если пытаться собрать максимально близко к текущему MVP только у CopterParts, я бы начал с такого набора:

| Узел | Выбор |
|---|---|
| Рама | `Holybro X500` только если подтверждается зазор под выбранные винты; иначе смотреть `Holybro X650` |
| Flight Controller | если не принципиален Mini: `Holybro Pixhawk 6C + PM07/GPS`; если нужен именно Mini kit — оставить Ozon/AliExpress |
| Моторы | `SunnySky X4108S KV380`, 4 шт |
| ESC | `FATJAY 50A 2-6S` или `Maytech MT50A-SBEC-FP32 50A`, 4 шт |
| Винты | сначала искать более дешёвые 14-15" пары; у CopterParts найденные T-Motor слишком дорогие |
| Аккумулятор | `6S 10000mAh`, но лучше с `XT90`; `Z POWER XT60` брать только после проверки тока |
| GPS | если нет в комплекте Pixhawk: `Matek M9N-5883` |
| RC | `RadioMaster Pocket M2 ELRS` + `RP4TD-M ELRS 2.4GHz` |
| Зарядка | `SkyRC S100 Neo` для старта или `HTRC T240 DUO`, если сразу несколько батарей |

## Что уточнить у продавца одним сообщением

Перед заказом я бы отправил продавцу такой список вопросов:

1. Есть ли в наличии `Pixhawk 6C Mini kit`, или только обычный `Pixhawk 6C`?
2. Что входит в `Комплект Holybro X500`: рама, моторы, ESC, винты, PDB, крепёж?
3. Влезают ли 15" пропеллеры на выбранную раму с безопасным зазором?
4. Есть ли более дешёвые пары 14-15" CW/CCW под вал 6 мм для `SunnySky X4108S KV380`?
5. Какой фактический разъём и C-rate у 6S 10000mAh батарей, есть ли варианты с `XT90`?
6. Поддерживает ли выбранный ESC обычный PWM/DShot от Pixhawk/ArduPilot, есть ли опыт с моторами 4108 и 14-15" винтами?
7. Какие кабели/переходники нужны для подключения `Matek M9N-5883` к Pixhawk 6C / Pixhawk 6C Mini?

