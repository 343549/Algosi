"""Сумма числа a и квадрата числа b (a + b²) (работа с файлами).

Читает из файла input.txt два числа, выводит результат a + b² в файл output.txt.
Ограничения: -1e9 <= a, b <= 1e9.
"""


def main() -> None:
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        data = input_file.read().strip().split()
    
    if len(data) != 2:
        raise ValueError("Ожидалось два числа")
    
    a, b = map(int, data)
    if not (-10**9 <= a <= 10**9 and -10**9 <= b <= 10**9):
        raise ValueError("Числа должны быть в диапазоне [-1e9, 1e9]")
    
    result = a + b * b
    
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(str(result))


if __name__ == "__main__":
    main()
