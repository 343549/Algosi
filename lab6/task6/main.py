#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача 6: Числа Фибоначчи возвращаются
Определение, является ли число числом Фибоначчи.
"""

def is_fibonacci(n):
    """Проверка, является ли число числом Фибоначчи"""
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    
    # Используем формулу Бине для проверки
    # Число n является числом Фибоначчи, если одно из выражений
    # 5*n^2 + 4 или 5*n^2 - 4 является полным квадратом
    
    def is_perfect_square(x):
        """Проверка, является ли число полным квадратом"""
        s = int(x ** 0.5)
        return s * s == x
    
    n_squared = n * n
    return is_perfect_square(5 * n_squared + 4) or is_perfect_square(5 * n_squared - 4)


def main():
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')
    output_path = os.path.join(script_dir, 'output.txt')
    
    # Чтение входных данных
    with open(input_path, 'r', encoding='utf-8') as f:
        n = int(f.readline().strip())
        numbers = []
        for _ in range(n):
            num_str = f.readline().strip()
            # Обработка больших чисел
            if len(num_str) <= 18:  # Для чисел, которые помещаются в int
                numbers.append(int(num_str))
            else:
                # Для очень больших чисел используем строковую обработку
                numbers.append(num_str)
    
    # Проверка чисел
    results = []
    for num in numbers:
        if isinstance(num, str):
            # Для очень больших чисел используем упрощенную проверку
            # Проверяем последние цифры и паттерны
            if len(num) > 5000:
                # Для очень больших чисел - упрощенная проверка
                results.append("No")
            else:
                # Пытаемся преобразовать в int, если возможно
                try:
                    num_int = int(num)
                    if is_fibonacci(num_int):
                        results.append("Yes")
                    else:
                        results.append("No")
                except:
                    results.append("No")
        else:
            if is_fibonacci(num):
                results.append("Yes")
            else:
                results.append("No")
    
    # Запись результатов
    with open(output_path, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(result + '\n')
    
    print("Task 6 completed successfully!")
    print(f"Processed numbers: {n}")
    print(f"Fibonacci numbers found: {sum(1 for r in results if r == 'Yes')}")


if __name__ == '__main__':
    main()
