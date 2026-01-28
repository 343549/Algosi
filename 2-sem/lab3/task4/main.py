"""
Задача 4. Порядок курсов
Студент: Джафари Хоссаин
Топологическая сортировка ориентированного ациклического графа (DAG).
"""

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

