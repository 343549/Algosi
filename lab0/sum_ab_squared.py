"""Сумма числа a и квадрата числа b (a + b²).

Читает из stdin строку с двумя числами, выводит результат a + b².
Ограничения: -1e9 <= a, b <= 1e9.
"""

import sys


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) != 2:
        sys.exit("Ожидалось два числа")
    a, b = map(int, data)
    if not (-10**9 <= a <= 10**9 and -10**9 <= b <= 10**9):
        sys.exit("Числа должны быть в диапазоне [-1e9, 1e9]")
    result = a + b * b
    print(result)


if __name__ == "__main__":
    main()
