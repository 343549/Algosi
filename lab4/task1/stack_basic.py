"""
Задача 1: Реализация стека
Вариант 19 — Алгоритмы и структуры данных, лаба 4

Формат ввода (input.txt):
M — количество команд (1 ≤ M ≤ 1_000_000)
Далее M строк вида:
  "+ N" — положить N в стек (|N| ≤ 10^9)
  "-"   — извлечь верхний элемент стека (гарантируется, что стек не пуст)

Формат вывода (output.txt):
Каждое извлечённое значение в отдельной строке, в порядке появления операций "-".

Сложность:
  - Время O(M)
  - Память O(M) в худшем случае
"""

from pathlib import Path


def process_commands(commands: list[str]) -> list[int]:
    """Выполняет команды стека и возвращает значения всех операций извлечения."""
    stack: list[int] = []
    popped: list[int] = []

    for cmd in commands:
        if not cmd:
            continue
        if cmd[0] == "+":
            # Формат: "+ N"
            _, value = cmd.split()
            stack.append(int(value))
        else:
            popped.append(stack.pop())

    return popped


def main() -> None:
    base = Path(__file__).parent
    with (base / "input.txt").open("r", encoding="utf-8") as f:
        m = int(f.readline().strip())
        commands = [f.readline().strip() for _ in range(m)]

    result = process_commands(commands)

    with (base / "output.txt").open("w", encoding="utf-8") as f:
        f.write("\n".join(map(str, result)))

    # Короткий вывод для отчёта
    print("Извлечённые элементы (по порядку):")
    for value in result:
        print(value)


if __name__ == "__main__":
    main()
