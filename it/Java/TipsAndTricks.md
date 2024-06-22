### String
String.join("delemeter", list)
"a".compareTo("b") < 0
"string".replace("old", "new")
"string".charAt(i)
"string".toCharArray()

### Character:
Character.toLowerCase('c')
Character.isAlphabetic('c')
Character.isDigit('5')
Character.isLetterOrDigit('c')

### StringBuilder:
sb.append("")
sb.setLength(0)
sb.delete(0, sb.length())
### Stream:
Collectors.grouptingBy(i -> i.key)

### Map:
**size**() -> int
**isEmpty**() -> boolean

**get**(K key) -> K
**getOrDefault**(K key, V defaultValue) -> V
**keySet**() -> Set\<K\>
**entrySet**() -> Set\<Map.Entry\<K, V\>\>
**values**() -> Collection\<V\>

**put**(K key, V value) -> V
**putAll**(Map m) -> void 
**putIfAbsent**(K key, V value) -> V 
    положит значение если пусто
**computeIfAbsent**(K key,  Function\<K, V\> mappingFunction) -> V 
    выполнит функцию, и положит ее результат если пусто
**computeIfPresent**(K key, BiFunction\<K, V, V\> remappingFunction) -> V 
    выполнит функцию, и положит ее результат если не пусто
**replace**(K key, V value) -> V 
**replace**(K key, V oldValue, V newValue) -> boolean 
**replaceAll**(BiFunction\<K, V, V\> function) -> void 

**remove**(K key) -> V 
**remove**(K key, V value) -> boolean 
**clear**() -> void 

**containsKey**(K key) -> boolean 
**containsValue**(V value) -> boolean 

**forEach**(BiConsumer\<K, V\> action) -> void 
**compute**(K key, BiFunction\<K, V, V\> remappingFunction) -> V 
    выполняет функцию, которая получает на вход ключ и старое значение. Если возвращает null, то запись удаляется. Если не null то заменяется или создается
**merge**(K key, V value, BiFunction\<V, V, V\> remappingFunction) -> V 
    проверяет есть ли что то по ключу. Если нет, то просто сохраняет переданное значение. Если есть то вызывает функцию и передает туда старое значение и value. Результат это функции сохраняет. Если она возвращает null то удаляет старый результат

**Map.of**(K k, V v) -> Map\<K, V\>
**Map.ofEntries**(Entry\<K, V\>...) -> Map\<K, V>
**Map.entry**(K k, V v) -> Entry\<K, V\>
**Map.copyOf**(Map<K, V> map) -> Map\<K, V\>

### Map.Entry<K, V>:
**getKey**() -> K
**getValue**() -> V
**setValue**() -> V

**Entry.comparingByKey**() -> Comparator\<Map.Entry\<K, V\>\>
**Entry.comparingByValue**() -> Comparator\<Map.Entry\<K, V\>\>
**Entry.comparingByKey**(Comparator\<K\> cmp) -> Comparator\<Map.Entry\<K, V\>\>
**Entry.comparingByValue**(Comparator\<V> cmp) -> Comparator\<Map.Entry\<K, V\>\>
**Entry.copyOf**(Map.Entry\<K, V\> e) -> Map.Entry\<K, V\>

### SortedMap:
**subMap**(K left, K right) -> SortedMap\<K, V\>
**headMap**(K key) -> SortedMap\<K, V\>
**tailMap**(k key) -> SortedMap\<K, V\>
**firstKey**() -> K
**lastKey**() -> K

### NavigableMap:
**lowerKey**(K key) -> K
**lowerEntry**(K key) -> Map.Entry\<K, V\>
    Возвращает энтри с ключем меньшим чем переданный (entry < key). Либо null если такого нет.
**floorKey**(K key) -> K
**floorEntry**(K key) -> Map.Entry\<K, V\>
    Возвращает энтри с ключом равным или меньшим чем переданный (entry <= key). Либо null если такого нет.
**ceilingKey**(K key) -> K
**ceilingEntry**(K key) -> Map.Entry\<K, V\>
    Возвращает энтри с ключом равным или большим чем переданный (entry >= key). Либо null если такого нет.
**higherKey**(K key) -> K
**higherEntry**(K key) -> Map.Entry\<K, V\>
    Возвращает энтри с ключом больше чем переданный (entry > key). Либо null если такого нет.

**firstEntry**() -> Map.Entry\<K, V\>
**lastEntry**() -> Map.Entry\<K, V\>

**pollFirstEntry**() -> Map.Entry\<K, V\>
**pollLastEntry**() -> Map.Entry\<K, V\>
    Возвращают и удаляют первый / последний элемент

**descendingKeySet**() -> NavigableSet\<K, V\>
**descendingMap**() -> NavigableMap\<K, V\>
    Возвращает сет / мапу с элементами в обратном порядке

**navigableKeySet**() -> NavigableSet\<K, V\>
**subMap**(K left, boolean bl, K right, boolean br) -> NavigableMap\<K, V\>
**subMap**(K left, K right) -> NavigableMap\<K, V\>
**headMap**(K k, boolean b) -> NavigableMap\<K, V\>
**headMap**(K k) -> NavigableMap\<K, V\>
**tailMap**(K k, boolean b) -> NavigableMap\<K, V\>
**tailMap**(K k) -> NavigableMap\<K, V\>
    Возвращает подмапу в диапазоне / меньше / больше чем переданный ключ. Включать переданный элемент можно указать в boolean

### Deque:
void addFirst(obj)
void addLast(obj)
E getFirst() - без удаления, NoSuchElementException
E getLast() - без удаления, NoSuchElementException
boolean offerFirst(obj)
boolean offerLast(obj)
E peekFirst() - возвращает без удаления или null
E peekLast() - возвращает без удаления или null
E pollFirst() - возвращает с удалением или null
E pollLast() - возвращает с удалением или null
E pop() возвращает с удалением из начала или NoSuchElementException
void push(obj) - добавляет в начало
E removeFirst() - возвращает с удаление, либо NoSuchElementException
E removeLast() - возвращает с удаление, либо NoSuchElementException

### Integer:
Integer.parseInt()
Integer.MAX_VALUE

### Math:
Math.sqrt()
Math.floor() - округление вниз

### Arrays:
Arrays.fill(array, value)

### Collections:
Collections.reverse(array)
Collections.binarySearch(list, value);

### Stack:
stack.pust() - добавляет элемент в стек
stack.pop() - возвращает элемент из стека и удаляет его
stack.peek() - возвращает элемент из стека но не удаляет его

### System:
System.arraycopy(src,  srcPos,  dest, destPos, length)

### Collection:
collection.toArray()

### Comparator:
**Comparator.comparing**(i -> func)
