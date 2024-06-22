YAML — это язык для сериализации данных, который отличается простым синтаксисом и позволяет хранить сложноорганизованные данные в компактном и читаемом формате. Рассказываем, как это пригодится для [DevOps](https://tproger.ru/curriculum/devops) и виртуализации.

### Советы
Строки всегда заключать в кавычки, так как интерпретатор может не верно определить тип данных, строка число или логическое значение

# Описание синтаксиса
### Группировка нескольких документов в одном файле
```yaml
---
player: playerOne
action: attack (miss)
---
player: playerTwo
action: attack (hit)
---
```
### Поддержка комментариев
```yaml
# Однострочный комментарий

# Многострочный
# комментарий
```
### Запись значений (ключ - значение)
```yaml
stringKey: string value
numberKey: 123
```
### Запись объектов
```yaml
objectKey:
  key1: value
  key2: value
```
### Явная типизация
Для явной типизации перед значением надо поставить !! с типом
```yaml
# Это значение преобразуется в int:
is-an-int: !!int 14.10
# Превращает любое значение в строку:
is-a-str: !!str 67.43
# Значение должно быть boolean:
is-a-bool: !!bool yes
```
### Типы данных
- int
- float
- boolean
- string
- null
Чиста возможно писать дополнительно в восмеричном и шестнацатиричном представлении, в научном виде, использовать бесконечность
```yaml
integer: 25
hex: 0x12d4 #равно 4820
octal: 023332 #равно 9946
float: 25.0
exponent: 12.3015e+05 #равно 1230150.0
boolean: Yes
string: "25"
infinity: .inf # преобразуется в бесконечность
neginf: -.Inf #преобразуется в минус бесконечность
not: .NAN #Not a Number
null: ~
```
### Строки
Доступен многострочная запись
```yaml
str: Hello World
data: |
   Это
   Отдельные
   Строки
data: >
   Это 
   один параграф
   текста
```
### Последовательности (массивы)
```yaml
shopping: 
- milk
- eggs
- juice
```
Либо в одну строку
```yaml
shopping: [milk, eggs, juice]
```
### Словари
```yaml
Employees: 
- dan:
    name: Dan D. Veloper
    job: Developer
    team: DevOps
- dora:
   name: Dora D. Veloper
   job: Project Manager
   team: Web Subscriptions
```
##### Ссылки:
[YAML за 5 минут: синтаксис и основные возможности](https://tproger.ru/translations/yaml-za-5-minut-sintaksis-i-osnovnye-vozmozhnosti)
[YAML из Ада](https://habr.com/ru/articles/710414/)
[yaml](https://en.wikipedia.org/wiki/YAML)

##### Связи:
[[IT]]
[[Формат данных]]