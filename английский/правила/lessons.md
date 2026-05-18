# Lessons

Таблица интервального повторения правил английского языка.

| Тема | Файл | next_review | repetitions | interval_days | ease_factor | last_grade | updated |
|---|---|---:|---:|---:|---:|---:|---:|
| Subject and Object Questions | [[Subject and Object Questions]] | 2026-05-19 | 1 | 1 | 2.6 | 5 | 2026-05-18 |

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
