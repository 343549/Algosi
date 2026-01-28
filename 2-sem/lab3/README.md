## Лабораторная работа 2–3. Графы  
Студент: **Джафари Хоссаин**  

В этой работе я решил три задачи по графам: №4 «Порядок курсов», №5 «Город с односторонним движением» и №14 «Автобусы».  
Для каждой задачи есть отдельная папка с исходным кодом на Python: `task4`, `task5`, `task14` (файл `main.py`), а также примерными файлами `input.txt` и `output.txt`.

## Задача 4. Порядок курсов

**Идея решения.**  
Дан ориентированный ациклический граф (DAG). Нужно вывести любой топологический порядок вершин.  
Я использовал **алгоритм Канна**: считаю входящие степени вершин, в очередь кладу все вершины с нулевой степенью, затем по очереди «удаляю» вершины и уменьшаю входящие степени у их соседей.

**Код (`task4/main.py`):**

```python
from collections import deque
import sys


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    g = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        g[u].append(v)
        indeg[v] += 1

    q: deque[int] = deque()
    for v in range(1, n + 1):
        if indeg[v] == 0:
            q.append(v)

    order: list[int] = []
    while q:
        v = q.popleft()
        order.append(v)
        for to in g[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)

    sys.stdout.write(" ".join(map(str, order)) + "\n")


if __name__ == "__main__":
    main()
```

**Пример запуска.**  
Вход:

```text
4 3
1 2
4 1
3 1
```

Выход (один из вариантов):

```text
4 3 1 2
```

**Вывод по задаче 4.**  
Топологическая сортировка позволяет упорядочить курсы так, чтобы все зависимости были соблюдены, и делается это за линейное время от количества вершин и рёбер.


## Задача 5. Город с односторонним движением

**Идея решения.**  
Нужно посчитать количество компонент сильной связности в ориентированном графе.  
Я использовал **алгоритм Косараджу**: сначала обхожу граф в глубину и записываю вершины по времени выхода, затем обхожу транспонированный граф в обратном порядке и считаю компоненты.

**Код (`task5/main.py`):**

```python
import sys
sys.setrecursionlimit(1_000_000)


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    g = [[] for _ in range(n + 1)]
    gr = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        g[u].append(v)
        gr[v].append(u)

    used = [False] * (n + 1)
    order: list[int] = []

    def dfs1(v: int) -> None:
        used[v] = True
        for to in g[v]:
            if not used[to]:
                dfs1(to)
        order.append(v)

    for v in range(1, n + 1):
        if not used[v]:
            dfs1(v)

    used = [False] * (n + 1)
    scc_count = 0

    def dfs2(v: int) -> None:
        used[v] = True
        for to in gr[v]:
            if not used[to]:
                dfs2(to)

    for v in reversed(order):
        if not used[v]:
            scc_count += 1
            dfs2(v)

    print(scc_count)


if __name__ == "__main__":
    main()
```

**Пример запуска.**  
Вход:

```text
4 4
1 2
4 1
2 3
3 1
```

Выход:

```text
2
```

**Вывод по задаче 5.**  
Компоненты сильной связности удобно искать через два прохода DFS: это даёт линейное по числу рёбер и вершин решение и позволяет понять, как разбивается граф на «сильно связанные» группы перекрёстков.

## Задача 14. Автобусы

**Идея решения.**  
Есть деревни и автобусные рейсы с указанием времени отправления и прибытия.  
Нужно минимальное время, когда можно добраться из деревни `d` в деревню `v`, начиная с момента времени 0.  
Я использовал модифицированный **алгоритм Беллмана–Форда**: храню раннее время прибытия в каждую деревню и многократно релаксирую все рейсы, но учитываю условие, что на рейс можно сесть только если мы успеваем к его отправлению (`dist[from] <= depart`).

**Код (`task14/main.py`):**

```python
import sys


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)

    n = int(next(it))     # число деревень
    d = int(next(it))     # стартовая деревня
    v = int(next(it))     # целевая деревня
    r = int(next(it))     # количество рейсов

    buses = []
    for _ in range(r):
        frm = int(next(it))
        depart = int(next(it))
        to = int(next(it))
        arrive = int(next(it))
        buses.append((frm, depart, to, arrive))

    INF = 10**9
    dist = [INF] * (n + 1)
    dist[d] = 0

    for _ in range(n - 1):
        changed = False
        for frm, depart, to, arrive in buses:
            if dist[frm] <= depart and arrive < dist[to]:
                dist[to] = arrive
                changed = True
        if not changed:
            break

    print(-1 if dist[v] == INF else dist[v])


if __name__ == "__main__":
    main()
```

**Пример запуска.**  
Вход (пример из условия):

```text
3
1 3
4
1 0 2 5
1 1 2 7
2 3 3 5
1 1 3 10
```

Выход:

```text
5
```

**Вывод по задаче 14.**  
Задачу с расписанием автобусов удобно рассматривать как граф с временными ограничениями: главное условие — успеть на рейс к моменту его отправления, после чего мы просто выбираем самые ранние времена прибытия.


## Общий вывод по работе

В этой лабораторной я научился применять разные алгоритмы на графах: топологическую сортировку, поиск компонент сильной связности и алгоритм кратчайшего пути с учётом времени.  
Все три задачи решаются за приемлемое время за счёт линейной или почти линейной сложности по числу вершин и рёбер.  
Работа показала, что даже сложные на первый взгляд задачи с зависимостями и расписанием можно свести к аккуратной работе с графами и стандартными алгоритмами.

