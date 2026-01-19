"""
Задача 6: Очередь с минимумом
Вариант 19 — Алгоритмы и структуры данных, лаба 4

Формат ввода (input.txt):
M — число команд (1 ≤ M ≤ 1_000_000)
Далее команды:
  "+ N" — добавить N в очередь (|N| ≤ 10^9)
  "-"   — извлечь элемент из очереди (гарантируется, что очередь не пуста)
  "?"   — вывести текущий минимум (гарантируется, что очередь не пуста)

Формат вывода (output.txt):
Каждый ответ на команду "?" в отдельной строке, в порядке появления запросов.

Сложность:
  - Все операции O(1) амортизировано
  - Память O(M) в худшем случае
"""

from pathlib import Path


class MinStack:
    """Стек, который вместе со значением хранит текущий минимум."""

    def __init__(self) -> None:
        self._data: list[tuple[int, int]] = []  # (value, current_min)

    def push(self, value: int) -> None:
        current_min = value if not self._data else min(value, self._data[-1][1])
        self._data.append((value, current_min))

    def pop(self) -> int:
        return self._data.pop()[0]

    def min(self) -> int:
        return self._data[-1][1]

    def __bool__(self) -> bool:  # позволяет писать "if stack:"
        return bool(self._data)


class MinQueue:
    """Очередь на двух стеках с поддержкой минимума за O(1) амортизировано."""

    def __init__(self) -> None:
        self._in = MinStack()
        self._out = MinStack()

    def _rebalance(self) -> None:
        if self._out:
            return
        while self._in:
            value = self._in.pop()
            # При перекладывании пересчитываем минимум для стека out
            current_min = value if not self._out else min(value, self._out.min())
            self._out._data.append((value, current_min))

    def push(self, value: int) -> None:
        self._in.push(value)

    def pop(self) -> int:
        self._rebalance()
        return self._out.pop()

    def get_min(self) -> int:
        # Минимум — минимум из верхушек обоих стеков
        mins = []
        if self._in:
            mins.append(self._in.min())
        if self._out:
            mins.append(self._out.min())
        return min(mins)


def process_commands(commands: list[str]) -> list[int]:
    queue = MinQueue()
    answers: list[int] = []

    for cmd in commands:
        if not cmd:
            continue
        if cmd[0] == "+":
            _, value = cmd.split()
            queue.push(int(value))
        elif cmd[0] == "-":
            queue.pop()
        else:  # "?"
            answers.append(queue.get_min())

    return answers


def main() -> None:
    base = Path(__file__).parent
    with (base / "input.txt").open("r", encoding="utf-8") as f:
        m = int(f.readline().strip())
        commands = [f.readline().strip() for _ in range(m)]

    result = process_commands(commands)

    with (base / "output.txt").open("w", encoding="utf-8") as f:
        f.write("\n".join(map(str, result)))

    print("Минимумы по запросам '?':")
    for value in result:
        print(value)


if __name__ == "__main__":
    main()
