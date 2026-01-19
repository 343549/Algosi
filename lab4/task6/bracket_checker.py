"""
Задача 4: Проверка скобочной последовательности (расширенная версия)
Вариант 19 — Алгоритмы и структуры данных, лаба 4

Формат ввода (input.txt):
Одна строка S (1 ≤ |S| ≤ 100_000), содержащая символы: латиница, цифры,
знаки препинания и скобки из набора []{}().

Формат вывода (output.txt):
  - "Success", если скобки корректны.
  - Индекс (от 1) первой несовпадающей скобки:
      * первой лишней закрывающей,
      * либо первой открывающей без пары (если закрывающих лишних нет).

Сложность:
  - Время O(|S|)
  - Память O(|S|) в худшем случае
"""

from pathlib import Path

PAIRS = {")": "(", "]": "[", "}": "{"}
OPENING = set(PAIRS.values())
ALL_BRACKETS = set(PAIRS) | OPENING


def check_brackets(text: str) -> str:
    """Возвращает 'Success' или индекс первой ошибочной скобки (строка)."""
    stack: list[tuple[str, int]] = []  # (скобка, позиция 1-based)

    for idx, ch in enumerate(text, 1):
        if ch in OPENING:
            stack.append((ch, idx))
        elif ch in PAIRS:
            if not stack:
                return str(idx)
            left, pos = stack.pop()
            if PAIRS[ch] != left:
                return str(idx)

    if stack:
        # Первая непарная открывающая — у основания стека
        return str(stack[0][1])

    return "Success"


def main() -> None:
    base = Path(__file__).parent
    with (base / "input.txt").open("r", encoding="utf-8") as f:
        text = f.readline().rstrip("\n")

    result = check_brackets(text)

    with (base / "output.txt").open("w", encoding="utf-8") as f:
        f.write(result)

    print("Результат проверки:", result)


if __name__ == "__main__":
    main()
