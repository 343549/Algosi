"""
Задача 14. Автобусы
Студент: Джафари Хоссаин
По расписанию автобусных рейсов нужно найти минимальное время,
за которое можно добраться из деревни d в деревню v.
"""

import sys


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)

    n = int(next(it))  # число деревень
    d = int(next(it))  # стартовая деревня
    v = int(next(it))  # целевая деревня
    r = int(next(it))  # количество рейсов

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

    # Модифицированный Беллман–Форд: учитываем время отправления рейса.
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

