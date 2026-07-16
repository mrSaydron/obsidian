# Lessons

Таблица интервального повторения правил английского языка.

| Тема | Файл | next_review | repetitions | interval_days | ease_factor | last_grade | updated |
|---|---|---:|---:|---:|---:|---:|---:|
| Subject and Object Questions | [[Subject and Object Questions]] | 2026-08-07 | 4 | 49 | 2.9 | 5 | 2026-06-19 |
| Tag Question | [[Tag Question]] | 2026-08-10 | 4 | 43 | 2.7 | 5 | 2026-06-28 |
| Alternative Question | [[Alternative Question]] | 2026-07-22 | 4 | 23 | 1.94 | 3 | 2026-06-29 |
| Past Simple | [[Past Simple]] | 2026-08-22 | 4 | 43 | 2.7 | 4 | 2026-07-10 |
| Prepositions of Time | [[Prepositions of Time]] | 2026-08-20 | 4 | 38 | 2.56 | 5 | 2026-07-13 |
| Used to | [[Used to]] | 2026-08-27 | 4 | 45 | 2.8 | 5 | 2026-07-13 |
| Past Simple and Past Continuous | [[Past Simple and Past Continuous]] | 2026-07-31 | 3 | 16 | 2.68 | 5 | 2026-07-15 |
| Past Continuous | [[Past Continuous]] | 2026-07-10 | 3 | 15 | 2.46 | 3 | 2026-06-25 |
| Present Simple and Present Continuous Questions | [[Present Simple and Present Continuous Questions]] | 2026-07-16 | 2 | 6 | 2.1 | 5 | 2026-07-10 |
| Stative and Action Verbs | [[Stative and Action Verbs]] | 2026-07-23 | 3 | 16 | 2.7 | 4 | 2026-07-07 |
| Future Simple and Be Going To | [[Future Simple and Be Going To]] | 2026-07-15 | 3 | 15 | 2.56 | 5 | 2026-06-30 |
| Word Order | [[Word Order]] | 2026-07-17 | 3 | 16 | 2.7 | 5 | 2026-07-01 |
| Modal Verbs: Should and Could | [[Modal Verbs Should and Could]] | 2026-07-19 | 3 | 16 | 2.7 | 5 | 2026-07-03 |
| Articles A-An, The, Zero Article | [[Articles A-An, The, Zero Article]] | 2026-07-14 | 2 | 6 | 2.5 | 4 | 2026-07-08 |

## Правила обновления SM-2

Начальные значения для новой темы:

- repetitions: 0
- interval_days: 1
- ease_factor: 2.5
- next_review: следующий день после добавления темы

После проверки ответа:

- Если оценка меньше 3:
  - repetitions = 0
  - interval_days = 1
  - ease_factor пересчитывается, но не ниже 1.3
- Если оценка 3 или выше:
  - repetitions += 1
  - interval_days:
    - 1-е успешное повторение: 1
    - 2-е успешное повторение: 6
    - далее: round(previous_interval_days * ease_factor)
  - ease_factor = max(1.3, ease_factor + (0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02)))

next_review = дата проверки + interval_days.
