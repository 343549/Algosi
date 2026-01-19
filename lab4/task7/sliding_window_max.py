"""
Задача 7: Максимум в движущейся последовательности (скользящее окно)
Вариант 19 — Алгоритмы и структуры данных, лаба 4

Формат ввода (input.txt):
n — количество элементов (1 ≤ n ≤ 100_000)
Вторая строка — n целых чисел ai (0 ≤ ai ≤ 100_000)
m — ширина окна (1 ≤ m ≤ n)

Формат вывода (output.txt):
Для каждого окна {a_i, ..., a_{i+m-1}} вывести максимум, значения разделить пробелом.

Сложность:
  - Время O(n)
  - Память O(m)
"""

from collections import deque
from pathlib import Path


def sliding_window_max(nums: list[int], window: int) -> list[int]:
    """Возвращает максимум для каждого окна длины window."""
    if window <= 0 or window > len(nums):
        raise ValueError("Некорректная ширина окна")

    dq: deque[int] = deque()  # храним индексы элементов в порядке убывания значений
    result: list[int] = []

    for i, value in enumerate(nums):
        # Удаляем индексы, вышедшие за окно
        while dq and dq[0] <= i - window:
            dq.popleft()

        # Поддерживаем убывание значений: убираем меньшие справа
        while dq and nums[dq[-1]] <= value:
            dq.pop()

        dq.append(i)

        # Добавляем максимум, когда окно уже полное
        if i + 1 >= window:
            result.append(nums[dq[0]])

    return result


def main() -> None:
    base = Path(__file__).parent
    with (base / "input.txt").open("r", encoding="utf-8") as f:
        n = int(f.readline().strip())
        nums = list(map(int, f.readline().strip().split()))
        window = int(f.readline().strip())

    assert len(nums) == n, "Количество чисел не совпадает с n"

    result = sliding_window_max(nums, window)

    with (base / "output.txt").open("w", encoding="utf-8") as f:
        f.write(" ".join(map(str, result)))

    print("Максимумы по окнам:")
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
