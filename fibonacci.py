"""Вычисление n-го числа Фибоначчи.

Читает из файла input.txt число n, выводит Fₙ в файл output.txt.
Ограничения: 0 ≤ n ≤ 45.

Определение последовательности Фибоначчи:
F₀ = 0
F₁ = 1
Fᵢ = Fᵢ₋₁ + Fᵢ₋₂ для i ≥ 2
"""


def calc_fib(n: int) -> int:
    """Вычисляет n-е число Фибоначчи с использованием динамического программирования.
    
    Использует итеративный подход для оптимальной временной сложности O(n)
    и пространственной сложности O(1).
    """
    if n <= 1:
        return n
    
    # Используем переменные для хранения двух предыдущих чисел
    prev_prev = 0  # F₀
    prev = 1       # F₁
    
    # Вычисляем числа последовательно от F₂ до Fₙ
    for i in range(2, n + 1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current
    
    return prev


def main() -> None:
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        n = int(input_file.read().strip())
    
    if not (0 <= n <= 45):
        raise ValueError("n должно быть в диапазоне [0, 45]")
    
    result = calc_fib(n)
    
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(str(result))


if __name__ == "__main__":
    main()
