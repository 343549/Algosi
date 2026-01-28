"""
Задача 5. Город с односторонним движением
Студент: Джафари Хоссаин
Подсчет количества компонент сильной связности в ориентированном графе.
"""

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
        gr[v].append(u)  # транспонированный граф

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

