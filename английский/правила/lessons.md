# Lessons

Таблица интервального повторения правил английского языка.

| Тема | Файл | next_review | repetitions | interval_days | ease_factor | last_grade | updated |
|---|---|---:|---:|---:|---:|---:|---:|
| Subject and Object Questions | [[Subject and Object Questions]] | 2027-01-29 | 5 | 142 | 2.9 | 4 | 2026-09-09 |
| Tag Question | [[Tag Question]] | 2026-12-26 | 4 | 35 | 2.48 | 5 | 2026-11-21 |
| Alternative Question | [[Alternative Question]] | 2027-01-17 | 6 | 53 | 1.78 | 4 | 2026-11-25 |
| Past Simple | [[Past Simple]] | 2027-01-17 | 5 | 120 | 2.8 | 5 | 2026-09-19 |
| Prepositions of Time | [[Prepositions of Time]] | 2026-12-27 | 5 | 101 | 2.66 | 5 | 2026-09-17 |
| Used to | [[Used to]] | 2027-01-25 | 5 | 120 | 2.66 | 3 | 2026-09-27 |
| Past Simple and Past Continuous | [[Past Simple and Past Continuous]] | 2027-02-07 | 5 | 116 | 2.64 | 3 | 2026-10-14 |
| Past Continuous | [[Past Continuous]] | 2026-12-30 | 5 | 101 | 2.66 | 5 | 2026-09-20 |
| Present Simple and Present Continuous Questions | [[Present Simple and Present Continuous Questions]] | 2026-12-21 | 5 | 69 | 2.3 | 4 | 2026-10-13 |
| Stative and Action Verbs | [[Stative and Action Verbs]] | 2027-02-03 | 5 | 120 | 2.8 | 5 | 2026-10-06 |
| Future Simple and Be Going To | [[Future Simple and Be Going To]] | 2026-12-27 | 5 | 97 | 2.56 | 4 | 2026-09-21 |
| Word Order | [[Word Order]] | 2027-01-23 | 5 | 116 | 2.7 | 4 | 2026-09-29 |
| Modal Verbs: Should and Could | [[Modal Verbs Should and Could]] | 2027-01-20 | 5 | 109 | 2.66 | 5 | 2026-10-03 |
| Articles A-An, The, Zero Article | [[Articles A-An, The, Zero Article]] | 2027-02-06 | 5 | 113 | 2.7 | 5 | 2026-10-16 |
| Intensifiers | [[Intensifiers]] | 2026-11-29 | 4 | 41 | 2.56 | 3 | 2026-10-19 |
| Zero Conditional | [[Zero Conditional]] | 2026-12-02 | 4 | 23 | 1.9 | 3 | 2026-11-09 |
| First Conditional | [[First Conditional]] | 2026-12-06 | 4 | 38 | 2.5 | 4 | 2026-10-29 |
| Adjectives that end in "-ed", "-ing" | [[Adjectives that end in -ed, -ing]] | 2026-11-26 | 3 | 17 | 2.8 | 5 | 2026-11-09 |
| Indefinite pronouns | [[Indefinite pronouns]] | 2026-11-30 | 3 | 14 | 2.36 | 4 | 2026-11-16 |
| defining relative clauses | [[defining relative clauses]] | 2026-12-02 | 3 | 15 | 2.46 | 4 | 2026-11-17 |
| non-defining relative clauses | [[non-defining relative clauses]] | 2026-11-24 | 2 | 6 | 2.6 | 4 | 2026-11-18 |
| Defining and Non-defining Relative Clauses | [[Defining and Non-defining Relative Clauses]] | 2026-11-28 | 2 | 6 | 2.6 | 4 | 2026-11-22 |
| Passive Voice - Present Simple | [[Passive Voice - Present Simple]] | 2026-11-26 | 1 | 1 | 2.5 | 4 | 2026-11-25 |
| Passive Voice - Past Simple | [[Passive Voice - Past Simple]] | 2026-11-27 | 1 | 1 | 2.6 | 5 | 2026-11-26 |
| Passive Voice - Future Simple | [[Passive Voice - Future Simple]] | 2026-11-19 | 0 | 1 | 2.5 | — | 2026-11-18 |
| Passive Voice - Present Continuous | [[Passive Voice - Present Continuous]] | 2026-11-19 | 0 | 1 | 2.5 | — | 2026-11-18 |
| Passive Voice - Past Continuous | [[Passive Voice - Past Continuous]] | 2026-11-19 | 0 | 1 | 2.5 | — | 2026-11-18 |
| Passive Voice - Present Perfect | [[Passive Voice - Present Perfect]] | 2026-11-19 | 0 | 1 | 2.5 | — | 2026-11-18 |
| Passive Voice - Past Perfect | [[Passive Voice - Past Perfect]] | 2026-11-19 | 0 | 1 | 2.5 | — | 2026-11-18 |
| Passive Voice - Questions in Simple Tenses | [[Passive Voice - Questions in Simple Tenses]] | 2026-11-19 | 0 | 1 | 2.5 | — | 2026-11-18 |
| Passive Voice - Questions in Continuous Tenses | [[Passive Voice - Questions in Continuous Tenses]] | 2026-11-19 | 0 | 1 | 2.5 | — | 2026-11-18 |
| Passive Voice - Questions in Perfect Tenses | [[Passive Voice - Questions in Perfect Tenses]] | 2026-11-19 | 0 | 1 | 2.5 | — | 2026-11-18 |

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
