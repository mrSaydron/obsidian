# Lessons

Таблица интервального повторения правил английского языка.

| Тема | Файл | next_review | repetitions | interval_days | ease_factor | last_grade | updated |
|---|---|---:|---:|---:|---:|---:|---:|
| Subject and Object Questions | [[Subject and Object Questions]] | 2026-08-07 | 4 | 49 | 2.9 | 5 | 2026-06-19 |
| Tag Question | [[Tag Question]] | 2026-06-22 | 3 | 16 | 2.6 | 5 | 2026-06-06 |
| Alternative Question | [[Alternative Question]] | 2026-06-22 | 3 | 12 | 2.08 | 3 | 2026-06-10 |
| Past Simple | [[Past Simple]] | 2026-06-13 | 2 | 6 | 2.6 | 5 | 2026-06-07 |
| Prepositions of Time | [[Prepositions of Time]] | 2026-06-14 | 2 | 6 | 2.46 | 5 | 2026-06-08 |
| Used to | [[Used to]] | 2026-06-15 | 2 | 6 | 2.6 | 5 | 2026-06-09 |
| Past Simple and Past Continuous | [[Past Simple and Past Continuous]] | 2026-06-19 | 0 | 1 | 2.38 | 2 | 2026-06-18 |
| Past Continuous | [[Past Continuous]] | 2026-06-18 | 2 | 6 | 2.6 | 5 | 2026-06-12 |
| Present Simple and Present Continuous Questions | [[Present Simple and Present Continuous Questions]] | 2026-06-21 | 2 | 6 | 2.46 | 3 | 2026-06-15 |
| Stative and Action Verbs | [[Stative and Action Verbs]] | 2026-06-15 | 1 | 1 | 2.6 | 5 | 2026-06-14 |
| Future Simple and Be Going To | [[Future Simple and Be Going To]] | 2026-06-22 | 2 | 6 | 2.46 | 5 | 2026-06-16 |
| Word Order | [[Word Order]] | 2026-06-23 | 2 | 6 | 2.6 | 4 | 2026-06-17 |
| Modal Verbs: Should and Could | [[Modal Verbs Should and Could]] | 2026-06-12 | 1 | 1 | 2.6 | 5 | 2026-06-11 |

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
