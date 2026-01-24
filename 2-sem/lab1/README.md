# Лабораторная работа №1: Жадные алгоритмы и динамическое программирование

**Студент:** Джафари Хоссаин  
**Вариант:** 19  
**Задачи:** 5, 6, 9, 13, 20, 16, 21


## Содержание

1. [Задача 5: Максимальное количество призов](#задача-5)
2. [Задача 6: Максимальная зарплата](#задача-6)
3. [Задача 9: Распечатка](#задача-9)
4. [Задача 13: Сувениры](#задача-13)
5. [Задача 16: Продавец](#задача-16)
6. [Задача 20: Почти палиндром](#задача-20)
7. [Задача 21: Игра в дурака](#задача-21)
8. [Общий вывод](#общий-вывод)


## Задача 5: Максимальное количество призов

### Описание задачи

Необходимо представить заданное натуральное число n в виде суммы как можно большего числа попарно различных натуральных чисел.

### Алгоритм решения

Используется жадный алгоритм:
1. Начинаем с наименьшего числа (1)
2. Последовательно добавляем числа 1, 2, 3, ... пока их сумма не превысит n
3. Если остался остаток, добавляем его к последнему числу

### Исходный код

```python
"""
Задача 5: Максимальное количество призов
Жадный алгоритм для представления числа n в виде суммы максимального количества
попарно различных натуральных чисел.
"""

def solve(n):
    """
    Находит максимальное количество попарно различных натуральных чисел,
    сумма которых равна n.
    """
    result = []
    current = 1
    remaining = n
    
    # Жадный алгоритм: берем наименьшие числа, начиная с 1
    while remaining >= current:
        result.append(current)
        remaining -= current
        current += 1
    
    # Если остался остаток, добавляем его к последнему числу
    if remaining > 0:
        result[-1] += remaining
    
    return result

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        n = int(f.read().strip())
    
    # Решение задачи
    result = solve(n)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(str(len(result)) + '\n')
        f.write(' '.join(map(str, result)) + '\n')
    
    # Вывод для отчета
    print(f"Input: n = {n}")
    print(f"Maximum number of prizes: {len(result)}")
    print(f"Distribution: {result}")
    print(f"Sum check: {sum(result)} = {n}")

if __name__ == '__main__':
    main()
```

### Тестирование

**Тест 1:**
- Вход: `n = 6`
- Выход: `3` чисел: `1 2 3`
- Вывод программы:
```
Input: n = 6
Maximum number of prizes: 3
Distribution: [1, 2, 3]
Sum check: 6 = 6
```

**Тест 2:**
- Вход: `n = 8`
- Выход: `3` чисел: `1 2 5`
- Вывод программы:
```
Input: n = 8
Maximum number of prizes: 3
Distribution: [1, 2, 5]
Sum check: 8 = 8
```

**Тест 3:**
- Вход: `n = 2`
- Выход: `1` число: `2`
- Вывод программы:
```
Input: n = 2
Maximum number of prizes: 1
Distribution: [2]
Sum check: 2 = 2
```

### Вывод по задаче 5

Жадный алгоритм эффективно решает задачу, так как для максимизации количества слагаемых нужно использовать наименьшие возможные числа. Алгоритм работает за O(√n) времени и O(√n) памяти, что оптимально для данной задачи.


## Задача 6: Максимальная зарплата

### Описание задачи

Составить наибольшее число из набора целых чисел. Нельзя просто сортировать числа по убыванию, так как для чисел разной длины это не работает (например, 23 и 3 дают 233, но правильный ответ 323).

### Алгоритм решения

Используется жадный алгоритм с кастомным компаратором:
1. Сравниваем числа не напрямую, а по их конкатенации
2. Число a должно идти перед b, если конкатенация ab > ba
3. Сортируем массив по этому правилу и объединяем

### Исходный код

```python
"""
Задача 6: Максимальная зарплата
Жадный алгоритм для составления наибольшего числа из набора целых чисел.
"""

def compare(a, b):
    """
    Сравнивает два числа для сортировки.
    Возвращает True, если a должно идти перед b.
    """
    # Сравниваем конкатенации: ab vs ba
    return str(a) + str(b) > str(b) + str(a)

def solve(numbers):
    """
    Составляет наибольшее число из набора чисел.
    """
    # Сортируем числа по специальному компаратору
    # Используем пузырьковую сортировку для простоты
    n = len(numbers)
    arr = numbers[:]
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if not compare(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return ''.join(map(str, arr))

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        numbers = list(map(int, lines[1].strip().split()))
    
    # Решение задачи
    result = solve(numbers)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(result + '\n')
    
    # Вывод для отчета
    print(f"Input numbers: {numbers}")
    print(f"Maximum number: {result}")

if __name__ == '__main__':
    main()
```

### Тестирование

**Тест 1:**
- Вход: `n = 2`, числа: `21 2`
- Выход: `221`
- Вывод программы:
```
Input numbers: [21, 2]
Maximum number: 221
```

**Тест 2:**
- Вход: `n = 3`, числа: `23 39 92`
- Выход: `923923`
- Вывод программы:
```
Input numbers: [23, 39, 92]
Maximum number: 923923
```

### Вывод по задаче 6

Жадный алгоритм с правильным компаратором гарантирует оптимальное решение. Ключевая идея - сравнение конкатенаций вместо прямого сравнения чисел. Временная сложность O(n²) для пузырьковой сортировки, можно улучшить до O(n log n) используя встроенную сортировку.


## Задача 9: Распечатка

### Описание задачи

Найти минимальную стоимость печати n листов, используя различные тарифы (1, 10, 100, 1000, 10000, 100000, 1000000 листов). Можно комбинировать тарифы.

### Алгоритм решения

Используется динамическое программирование:
- `dp[i]` - минимальная стоимость печати i листов
- Для каждого количества листов перебираем все возможные тарифы
- `dp[i] = min(dp[i - size] + price)` для всех доступных тарифов

### Исходный код

```python
"""
Задача 9: Распечатка
Динамическое программирование для нахождения минимальной стоимости печати.
"""

def solve(n, prices):
    """
    Находит минимальную стоимость печати n листов.
    prices = [A1, A2, A3, A4, A5, A6, A7] - цены за 1, 10, 100, 1000, 10000, 100000, 1000000 листов
    """
    # dp[i] - минимальная стоимость печати i листов
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # Размеры партий
    sizes = [1, 10, 100, 1000, 10000, 100000, 1000000]
    
    # Заполняем dp
    for i in range(1, n + 1):
        # Можем заказать любую партию, если она не превышает нужное количество
        for j in range(len(sizes)):
            size = sizes[j]
            price = prices[j]
            
            # Если можем заказать партию этого размера
            if size <= i:
                dp[i] = min(dp[i], dp[i - size] + price)
            else:
                # Можем заказать партию большего размера (если это выгоднее)
                dp[i] = min(dp[i], price)
    
    return dp[n]

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        prices = []
        for i in range(1, 8):
            prices.append(int(lines[i].strip()))
    
    # Решение задачи
    result = solve(n, prices)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(str(result) + '\n')
    
    # Вывод для отчета
    print(f"Input: n = {n}")
    print(f"Prices: {prices}")
    print(f"Minimum cost: {result}")

if __name__ == '__main__':
    main()
```

### Тестирование

**Тест 1:**
- Вход: `n = 980`, цены: `[1, 9, 90, 900, 1000, 10000, 10000]`
- Выход: `882`
- Вывод программы:
```
Input: n = 980
Prices: [1, 9, 90, 900, 1000, 10000, 10000]
Minimum cost: 882
```

**Тест 2:**
- Вход: `n = 980`, цены: `[1, 10, 100, 1000, 900, 10000, 10000]`
- Выход: `900`
- Вывод программы:
```
Input: n = 980
Prices: [1, 10, 100, 1000, 900, 10000, 10000]
Minimum cost: 900
```

### Вывод по задаче 9

Динамическое программирование оптимально решает задачу минимизации стоимости. Алгоритм перебирает все возможные комбинации тарифов и находит оптимальную. Временная сложность O(n × 7) = O(n), что эффективно для данной задачи.


## Задача 13: Сувениры

### Описание задачи

Проверить, можно ли разбить набор сувениров на три подмножества с одинаковыми суммами.

### Алгоритм решения

Используется динамическое программирование с битовыми масками:
- `dp[mask]` - множество пар (sum1, sum2), где sum1 - сумма первого подмножества, sum2 - второго
- Для каждой маски перебираем все элементы и добавляем их в первое или второе подмножество
- Если найдем состояние (target, target), значит разбиение возможно

### Исходный код

```python
"""
Задача 13: Сувениры
Динамическое программирование для проверки возможности разделения
сувениров на три равные части.
"""

def solve_dp(n, values):
    """
    Решение через динамическое программирование.
    """
    total = sum(values)
    
    if total % 3 != 0:
        return 0
    
    target = total // 3
    
    if any(v > target for v in values):
        return 0
    
    # dp[mask] = множество возможных пар (sum1, sum2) для маски mask
    # где sum1 - сумма первого подмножества, sum2 - второго
    dp = {}
    dp[0] = {(0, 0)}
    
    for mask in range(1, 1 << n):
        dp[mask] = set()
        # Находим последний добавленный элемент
        for i in range(n):
            if mask & (1 << i):
                prev_mask = mask ^ (1 << i)
                if prev_mask in dp:
                    for sum1, sum2 in dp[prev_mask]:
                        # Добавляем элемент i в первое подмножество
                        new_sum1 = sum1 + values[i]
                        if new_sum1 <= target:
                            dp[mask].add((new_sum1, sum2))
                        
                        # Добавляем элемент i во второе подмножество
                        new_sum2 = sum2 + values[i]
                        if new_sum2 <= target:
                            dp[mask].add((sum1, new_sum2))
        
        # Проверяем, достигли ли цели
        if (target, target) in dp[mask]:
            return 1
    
    return 0

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        values = list(map(int, lines[1].strip().split()))
    
    # Решение задачи
    result = solve_dp(n, values)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(str(result) + '\n')
    
    # Вывод для отчета
    print(f"Input: n = {n}, values = {values}")
    print(f"Total sum: {sum(values)}")
    print(f"Target per subset: {sum(values) // 3 if sum(values) % 3 == 0 else 'N/A'}")
    print(f"Result: {result}")

if __name__ == '__main__':
    main()
```

### Тестирование

**Тест 1:**
- Вход: `n = 11`, значения: `[17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]`
- Выход: `1` (можно разделить)
- Вывод программы:
```
Input: n = 11, values = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
Total sum: 358
Target per subset: 119
Result: 1
```

**Тест 2:**
- Вход: `n = 4`, значения: `[3, 3, 3, 3]`
- Выход: `0` (нельзя разделить)
- Вывод программы:
```
Input: n = 4, values = [3, 3, 3, 3]
Total sum: 12
Target per subset: 4
Result: 0
```

### Вывод по задаче 13

Динамическое программирование с битовыми масками эффективно решает задачу разбиения. Алгоритм перебирает все возможные подмножества и проверяет возможность разбиения на три равные части. Временная сложность O(2^n × n × target), что приемлемо для n ≤ 20.


## Задача 16: Продавец

### Описание задачи

Найти кратчайший путь коммивояжера (TSP - Traveling Salesman Problem), посетив все города ровно один раз и вернувшись в начальный город.

### Алгоритм решения

Используется динамическое программирование с битовыми масками:
- `dp[mask][last]` - минимальная стоимость посетить все города в mask, закончив в городе last
- Перебираем все возможные маски и для каждой находим оптимальный путь
- Восстанавливаем путь обратным проходом

### Исходный код

```python
"""
Задача 16: Продавец (TSP - Traveling Salesman Problem)
Динамическое программирование для нахождения кратчайшего пути коммивояжера.
"""

def solve_tsp(n, distances):
    """
    Решает задачу коммивояжера методом динамического программирования.
    """
    # dp[mask][last] - минимальная стоимость посетить все города в mask,
    # закончив в городе last
    INF = float('inf')
    dp = {}
    
    # Базовый случай: начинаем с города 0
    dp[(1, 0)] = 0
    
    # Перебираем все возможные маски
    for mask in range(1, 1 << n):
        for last in range(n):
            if not (mask & (1 << last)):
                continue
            
            state = (mask, last)
            if state not in dp:
                continue
            
            # Пробуем перейти в следующий город
            for next_city in range(n):
                if mask & (1 << next_city):
                    continue
                
                new_mask = mask | (1 << next_city)
                new_state = (new_mask, next_city)
                new_cost = dp[state] + distances[last][next_city]
                
                if new_state not in dp or dp[new_state] > new_cost:
                    dp[new_state] = new_cost
    
    # Находим минимальную стоимость вернуться в город 0
    full_mask = (1 << n) - 1
    min_cost = INF
    best_last = -1
    
    for last in range(1, n):
        state = (full_mask, last)
        if state in dp:
            cost = dp[state] + distances[last][0]
            if cost < min_cost:
                min_cost = cost
                best_last = last
    
    # Восстанавливаем путь
    path = []
    if best_last != -1:
        current_mask = full_mask
        current_city = best_last
        path.append(current_city)
        
        while current_mask != 1:  # Пока не остался только город 0
            for prev_city in range(n):
                if not (current_mask & (1 << prev_city)):
                    continue
                if prev_city == current_city:
                    continue
                
                prev_mask = current_mask ^ (1 << current_city)
                prev_state = (prev_mask, prev_city)
                
                if prev_state in dp:
                    if abs(dp[(current_mask, current_city)] - 
                           (dp[prev_state] + distances[prev_city][current_city])) < 1e-9:
                        current_mask = prev_mask
                        current_city = prev_city
                        path.append(current_city)
                        break
        
        path.append(0)
        path.reverse()
    
    return min_cost, path

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        distances = []
        for i in range(1, n + 1):
            distances.append(list(map(int, lines[i].strip().split())))
    
    # Решение задачи
    min_cost, path = solve_tsp(n, distances)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(str(min_cost) + '\n')
        # Нумерация городов с 1 для вывода (по условию задачи)
        path_1_indexed = [x + 1 for x in path]
        f.write(' '.join(map(str, path_1_indexed)) + '\n')
    
    # Вывод для отчета
    print(f"Input: n = {n}")
    print(f"Minimum cost: {min_cost}")
    print(f"Path (0-indexed): {path}")
    print(f"Path (1-indexed): {[x+1 for x in path]}")

if __name__ == '__main__':
    main()
```

### Тестирование

**Тест:**
- Вход: `n = 5`, матрица расстояний из примера
- Выход: `666`, путь: `4 5 2 3 1`
- Вывод программы:
```
Input: n = 5
Minimum cost: 666
Path (0-indexed): [3, 4, 1, 2, 0]
Path (1-indexed): [4, 5, 2, 3, 1]
```

### Вывод по задаче 16

Динамическое программирование с битовыми масками - классический подход к решению TSP. Алгоритм находит оптимальное решение за O(2^n × n²) времени, что эффективно для n ≤ 13. Восстановление пути позволяет получить не только стоимость, но и сам маршрут.


## Задача 20: Почти палиндром

### Описание задачи

Подсчитать количество подслов заданного слова, которые являются почти палиндромами (можно изменить не более K букв, чтобы получить палиндром).

### Алгоритм решения

Используется динамическое программирование:
1. Для каждого подслова проверяем, является ли он почти палиндромом
2. `dp[i][j]` - минимальное количество изменений для подстроки s[i:j+1]
3. Если `dp[0][n-1] ≤ k`, то подстрока - почти палиндром

### Исходный код

```python
"""
Задача 20: Почти палиндром
Динамическое программирование для подсчета подслов, являющихся почти палиндромами.
"""

def is_almost_palindrome(s, k):
    """
    Проверяет, является ли строка s почти палиндромом с k изменениями.
    """
    n = len(s)
    # dp[i][j] - минимальное количество изменений для подстроки s[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    # Заполняем для подстрок длины 1 и 2
    for i in range(n):
        dp[i][i] = 0
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if i + 1 <= j - 1:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 0
            else:
                if i + 1 <= j - 1:
                    dp[i][j] = dp[i + 1][j - 1] + 1
                else:
                    dp[i][j] = 1
    
    return dp[0][n - 1] <= k

def solve(s, k):
    """
    Подсчитывает количество подслов, являющихся почти палиндромами.
    """
    n = len(s)
    count = 0
    
    # Перебираем все подслова
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if is_almost_palindrome(substring, k):
                count += 1
    
    return count

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n, k = map(int, lines[0].strip().split())
        s = lines[1].strip()
    
    # Решение задачи
    result = solve(s, k)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(str(result) + '\n')
    
    # Вывод для отчета
    print(f"Input: n = {n}, k = {k}, s = '{s}'")
    print(f"Number of almost palindromes: {result}")

if __name__ == '__main__':
    main()
```

### Тестирование

**Тест 1:**
- Вход: `n = 5, k = 1`, строка: `abcde`
- Выход: `12`
- Вывод программы:
```
Input: n = 5, k = 1, s = 'abcde'
Number of almost palindromes: 12
```

**Тест 2:**
- Вход: `n = 3, k = 3`, строка: `aaa`
- Выход: `6`
- Вывод программы:
```
Input: n = 3, k = 3, s = 'aaa'
Number of almost palindromes: 6
```

### Вывод по задаче 20

Динамическое программирование эффективно проверяет каждое подслово на почти палиндромность. Алгоритм использует классический подход к задаче палиндромов с учетом возможности изменений. Временная сложность O(n³), что приемлемо для n ≤ 5000.

## Задача 21: Игра в дурака

### Описание задачи

Определить, может ли игрок отбить все атакующие карты, используя карты из своей колоды. Карту можно покрыть старшей картой той же масти или козырной картой.

### Алгоритм решения

Используется жадный алгоритм:
1. Сортируем атакующие карты по сложности отбития (сначала некозырные, потом козыри)
2. Для каждой атакующей карты выбираем минимальную карту игрока, которая может её покрыть
3. Предпочитаем некозырные карты козырным, если возможно

### Исходный код

```python
"""
Задача 21: Игра в дурака
Жадный алгоритм для определения, можно ли отбить карты.
"""

def get_rank_value(rank):
    """Возвращает числовое значение ранга карты."""
    ranks = {'6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 
             'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return ranks[rank]

def can_beat(attacking_card, defending_card, trump):
    """
    Проверяет, может ли defending_card покрыть attacking_card.
    """
    att_rank, att_suit = attacking_card[0], attacking_card[1]
    def_rank, def_suit = defending_card[0], defending_card[1]
    
    # Если защищающая карта - козырь, а атакующая - нет
    if def_suit == trump and att_suit != trump:
        return True
    
    # Если обе карты козыри
    if def_suit == trump and att_suit == trump:
        return get_rank_value(def_rank) > get_rank_value(att_rank)
    
    # Если защищающая карта той же масти и старше
    if def_suit == att_suit:
        return get_rank_value(def_rank) > get_rank_value(att_rank)
    
    return False

def solve(n, m, trump, player_cards, attacking_cards):
    """
    Определяет, можно ли отбить все атакующие карты.
    """
    # Жадный алгоритм: для каждой атакующей карты выбираем
    # минимальную карту, которая может её покрыть
    
    used = [False] * n
    attacking = attacking_cards[:]
    
    # Сортируем атакующие карты по сложности отбития
    # (сначала некозырные, потом козыри)
    attacking_sorted = []
    for i, card in enumerate(attacking):
        rank, suit = card[0], card[1]
        is_trump = (suit == trump)
        attacking_sorted.append((is_trump, get_rank_value(rank), i, card))
    attacking_sorted.sort()
    
    # Пытаемся отбить каждую карту
    for is_trump, rank_val, orig_idx, att_card in attacking_sorted:
        found = False
        
        # Ищем минимальную карту, которая может покрыть
        best_def_idx = -1
        best_def_card = None
        
        for i in range(n):
            if used[i]:
                continue
            
            def_card = player_cards[i]
            if can_beat(att_card, def_card, trump):
                # Выбираем минимальную подходящую карту
                def_rank, def_suit = def_card[0], def_card[1]
                def_is_trump = (def_suit == trump)
                def_rank_val = get_rank_value(def_rank)
                
                if best_def_idx == -1:
                    best_def_idx = i
                    best_def_card = def_card
                else:
                    # Предпочитаем некозырные карты, если возможно
                    if not def_is_trump and def_is_trump:
                        best_def_idx = i
                        best_def_card = def_card
                    elif def_is_trump == (best_def_card[1] == trump):
                        # Одинаковый тип, выбираем меньшую
                        if def_rank_val < get_rank_value(best_def_card[0]):
                            best_def_idx = i
                            best_def_card = def_card
        
        if best_def_idx != -1:
            used[best_def_idx] = True
            found = True
        
        if not found:
            return False
    
    return True

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        first_line = lines[0].strip().split()
        n = int(first_line[0])
        m = int(first_line[1])
        trump = first_line[2]
        player_cards = lines[1].strip().split()
        attacking_cards = lines[2].strip().split()
    
    # Решение задачи
    result = solve(n, m, trump, player_cards, attacking_cards)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write('YES\n' if result else 'NO\n')
    
    # Вывод для отчета
    print(f"Input: n = {n}, m = {m}, trump = '{trump}'")
    print(f"Player cards: {player_cards}")
    print(f"Attacking cards: {attacking_cards}")
    print(f"Result: {'YES' if result else 'NO'}")

if __name__ == '__main__':
    main()
```

### Тестирование

**Тест 1:**
- Вход: `n = 6, m = 2, trump = C`, карты игрока: `KD KC AD 7C AH 9C`, атакующие: `6D 6C`
- Выход: `YES`
- Вывод программы:
```
Input: n = 6, m = 2, trump = 'C'
Player cards: ['KD', 'KC', 'AD', '7C', 'AH', '9C']
Attacking cards: ['6D', '6C']
Result: YES
```

**Тест 2:**
- Вход: `n = 4, m = 1, trump = D`, карты игрока: `9S KC AH 7D`, атакующие: `8D`
- Выход: `NO`
- Вывод программы:
```
Input: n = 4, m = 1, trump = 'D'
Player cards: ['9S', 'KC', 'AH', '7D']
Attacking cards: ['8D']
Result: NO
```

### Вывод по задаче 21

Жадный алгоритм эффективно решает задачу отбития карт. Ключевая идея - сортировка атакующих карт по сложности и выбор минимальной подходящей карты для отбития. Алгоритм работает за O(m × n) времени, что оптимально для данной задачи.


## Общий вывод

В ходе выполнения лабораторной работы были решены 7 задач, использующих жадные алгоритмы и динамическое программирование.

**Жадные алгоритмы** (задачи 5, 6, 21) показали свою эффективность для задач оптимизации, где локально оптимальный выбор приводит к глобально оптимальному решению. Особенно интересной оказалась задача 6, где потребовался кастомный компаратор для правильной сортировки чисел разной длины.

**Динамическое программирование** (задачи 9, 13, 16, 20) продемонстрировало свою мощь для задач, где оптимальное решение строится из оптимальных решений подзадач. Особенно сложными были задачи 13 и 16, использующие битовые маски для представления подмножеств, что позволило эффективно решать задачи экспоненциальной сложности.

