# Лабораторная работа №5: Пирамида (куча) и приоритеты

**Вариант:** 19  
**Студент:** Джафари Хоссаин

## Содержание
1. [Введение](#введение)  
2. [Задача 5: Планировщик задач](#задача-5-планировщик-задач)  
3. [Задача 6: Очередь с приоритетами](#задача-6-очередь-с-приоритетами)  
4. [Общий вывод](#общий-вывод)  
5. [Структура проекта](#структура-проекта)  
6. [Запуск](#запуск)


## Введение
Работа посвящена двоичной куче (пирамида) и её применению: планирование задач по времени освобождения потока и расширенная очередь с приоритетами с операцией `decrease-key`. Вариант 19 требует решить задачи №5 и №6 из методички.


## Задача 5: Планировщик задач
### Постановка
Даны `n` потоков и `m` задач с временами исполнения `t[i]`. Поток, который освободится раньше всех, берёт следующую задачу; при одновременном освобождении выбирается поток с меньшим индексом. Для каждой задачи нужно вывести `индекс_потока` и время старта.

### Алгоритм
Мин-куча по парам `(time_free, thread_id)`:
- Инициализация: все потоки свободны в момент `0`.
- Для каждой задачи: извлекаем минимум, печатаем `(thread_id, time_free)`, возвращаем поток с `time_free + t[i]`.

### Код
```1:28:task5/main.py
import sys
import heapq


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    times = list(map(int, data[2:2 + m]))

    # Min-heap by (next_free_time, thread_index)
    heap = [(0, i) for i in range(n)]
    heapq.heapify(heap)

    out_lines: list[str] = []
    for t in times:
        free_time, idx = heapq.heappop(heap)
        out_lines.append(f\"{idx} {free_time}\")
        heapq.heappush(heap, (free_time + t, idx))

    sys.stdout.write(\"\\n\".join(out_lines))


if __name__ == \"__main__\":
    main()
```

### Сложность
- Время: `O(m log n)`  
- Память: `O(n)`

### Пример
Вход:  
```
2 5
1 2 3 4 5
```
Выход:  
```
0 0
1 0
0 1
1 2
0 4
```


## Задача 6: Очередь с приоритетами
### Постановка
Операции с очередью:
- `A x` — добавить `x`
- `X` — извлечь минимум (или `*`, если очередь пуста)
- `D i y` — уменьшить значение элемента, добавленного в строке `i+1` входа, до `y` (элемент гарантированно в очереди, `y` меньше старого значения)

### Алгоритм
Мин-куча + таблица позиций:
- Элементы кучи: `(value, id)`; `id` — уникальный номер операции `A`.
- `pos[id]` хранит текущий индекс в куче → даёт `O(1)` доступ для `D`.
- При уменьшении ключа меняем значение и делаем `sift_up`, обновляя `pos` при свапах.

### Код
```1:121:task6/main.py
import sys


class MinHeap:
    # heap elements: [value, id]
    def __init__(self) -> None:
        self.h: list[list[int]] = []
        self.pos: dict[int, int] = {}  # id -> index in heap

    def _swap(self, i: int, j: int) -> None:
        self.h[i], self.h[j] = self.h[j], self.h[i]
        self.pos[self.h[i][1]] = i
        self.pos[self.h[j][1]] = j

    def _less(self, i: int, j: int) -> bool:
        # compare by value, then by id (doesn't matter much, but stable)
        if self.h[i][0] != self.h[j][0]:
            return self.h[i][0] < self.h[j][0]
        return self.h[i][1] < self.h[j][1]

    def _sift_up(self, i: int) -> None:
        while i > 0:
            p = (i - 1) // 2
            if self._less(i, p):
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self.h)
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            smallest = i

            if l < n and self._less(l, smallest):
                smallest = l
            if r < n and self._less(r, smallest):
                smallest = r

            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def push(self, value: int, item_id: int) -> None:
        self.h.append([value, item_id])
        i = len(self.h) - 1
        self.pos[item_id] = i
        self._sift_up(i)

    def extract_min(self) -> int | None:
        if not self.h:
            return None
        res_val, res_id = self.h[0]
        last = self.h.pop()
        self.pos.pop(res_id, None)
        if self.h:
            self.h[0] = last
            self.pos[self.h[0][1]] = 0
            self._sift_down(0)
        return res_val

    def decrease_key(self, item_id: int, new_value: int) -> None:
        i = self.pos[item_id]
        self.h[i][0] = new_value
        self._sift_up(i)


def main() -> None:
    inp = sys.stdin.buffer
    out_lines: list[str] = []

    first = inp.readline()
    if not first:
        return
    q = int(first)

    heap = MinHeap()
    # add_id_by_op_line[k] = item_id of element added by operation line k (k starts from 1)
    # Operation lines are lines AFTER the first line with q.
    add_id_by_op_line: list[int | None] = [None] * (q + 1)  # 1-based op lines
    next_add_id = 1

    for op_line_no in range(1, q + 1):
        line = inp.readline()
        if not line:
            break
        parts = line.split()
        if not parts:
            continue

        op = parts[0].decode()
        if op == "A":
            x = int(parts[1])
            item_id = next_add_id
            next_add_id += 1
            add_id_by_op_line[op_line_no] = item_id
            heap.push(x, item_id)
        elif op == "X":
            v = heap.extract_min()
            out_lines.append("*" if v is None else str(v))
        elif op == "D":
            x = int(parts[1])  # x means: line number of A is x+1
            y = int(parts[2])
            # File line 1 is q, file line (x+1) corresponds to operation line x.
            a_op_line = x
            item_id = add_id_by_op_line[a_op_line]
            # by statement: this A exists and not removed, and y is smaller
            heap.decrease_key(int(item_id), y)
        else:
            # unknown op: ignore
            pass

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
```


### Пример
Вход:  
```
8
A 3
A 4
A 2
X
D 2 1
X
X
X
```
Выход:  
```
2
1
3
*
```


## Общий вывод
- Оба решения опираются на **мин-кучу** для быстрого выбора минимального элемента.
- В планировщике это поток с минимальным временем готовности; в очереди — минимальный ключ.
- Для операции `D` нужна таблица позиций, чтобы менять ключ за `O(log n)` без линейного поиска.


## Структура проекта
```
lab5/
├── task5/
│   ├── main.py        # решение задачи 5
│   └── README.md      # краткий запуск (опционально)
├── task6/
│   ├── main.py        # решение задачи 6
│   └── README.md      # краткий запуск (опционально)
└── README.md          # этот отчёт
```

## Запуск
Из корня:
- Задача 5: `python task5/main.py < input.txt`
- Задача 6: `python task6/main.py < input.txt`
