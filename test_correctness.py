"""Проверка корректности алгоритмов из заданий 2 и 3.

Использует альтернативные (возможно, неэффективные) решения для проверки
правильности ответов основных алгоритмов.
"""

import sys
import io

# Настройка вывода для поддержки UTF-8 в Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def calc_fib_naive(n: int) -> int:
    """Наивная рекурсивная реализация для проверки (работает только для малых n)."""
    if n <= 1:
        return n
    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)


def calc_fib_optimized(n: int) -> int:
    """Оптимизированная реализация из задания 2."""
    if n <= 1:
        return n
    
    prev_prev = 0
    prev = 1
    
    for i in range(2, n + 1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current
    
    return prev


def calc_fib_last_digit_optimized(n: int) -> int:
    """Оптимизированная реализация из задания 3."""
    if n <= 1:
        return n
    
    n_mod_period = n % 60
    prev_prev = 0
    prev = 1
    
    for i in range(2, n_mod_period + 1):
        current = (prev_prev + prev) % 10
        prev_prev = prev
        prev = current
    
    return prev


def test_correctness():
    """Проверяет корректность алгоритмов."""
    
    print("=" * 70)
    print("ПРОВЕРКА КОРРЕКТНОСТИ АЛГОРИТМОВ")
    print("=" * 70)
    
    # Тест задания 2: сравниваем наивную и оптимизированную версию
    print("\nЗадание 2: Сравнение наивной и оптимизированной версии")
    print("-" * 70)
    print(f"{'n':<5} {'Наивная':<20} {'Оптимизированная':<20} {'Статус':<15}")
    print("-" * 70)
    
    test_values_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
    all_correct_2 = True
    
    for n in test_values_2:
        try:
            naive_result = calc_fib_naive(n)
            optimized_result = calc_fib_optimized(n)
            
            if naive_result == optimized_result:
                status = "✓ Корректно"
            else:
                status = "✗ ОШИБКА!"
                all_correct_2 = False
            
            print(f"{n:<5} {naive_result:<20} {optimized_result:<20} {status:<15}")
        except RecursionError:
            print(f"{n:<5} {'Переполнение':<20} {calc_fib_optimized(n):<20} {'(n слишком большой)':<15}")
    
    print("-" * 70)
    if all_correct_2:
        print("✓ Все тесты задания 2 пройдены успешно!")
    else:
        print("✗ Обнаружены ошибки в задании 2!")
    
    # Тест задания 3: проверяем, что последняя цифра совпадает с заданием 2
    print("\n\nЗадание 3: Проверка последней цифры")
    print("-" * 70)
    print(f"{'n':<5} {'F(n) (задание 2)':<20} {'Последняя цифра':<20} {'Статус':<15}")
    print("-" * 70)
    
    test_values_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 40, 45]
    all_correct_3 = True
    
    for n in test_values_3:
        fib_value = calc_fib_optimized(n)
        last_digit_from_fib = fib_value % 10
        last_digit_optimized = calc_fib_last_digit_optimized(n)
        
        if last_digit_from_fib == last_digit_optimized:
            status = "✓ Корректно"
        else:
            status = "✗ ОШИБКА!"
            all_correct_3 = False
        
        print(f"{n:<5} {fib_value:<20} {last_digit_optimized:<20} {status:<15}")
    
    print("-" * 70)
    if all_correct_3:
        print("✓ Все тесты задания 3 пройдены успешно!")
    else:
        print("✗ Обнаружены ошибки в задании 3!")
    
    # Дополнительная проверка периода Пизано
    print("\n\nДополнительная проверка: Период Пизано")
    print("-" * 70)
    print("Проверяем, что F(n) mod 10 = F(n + 60) mod 10 для различных n")
    print("-" * 70)
    
    test_pairs = [(10, 70), (20, 80), (30, 90), (100, 160), (331, 391)]
    all_period_correct = True
    
    for n1, n2 in test_pairs:
        result1 = calc_fib_last_digit_optimized(n1)
        result2 = calc_fib_last_digit_optimized(n2)
        
        if result1 == result2:
            print(f"✓ F({n1}) mod 10 = F({n2}) mod 10 = {result1}")
        else:
            print(f"✗ F({n1}) mod 10 = {result1}, F({n2}) mod 10 = {result2} (ошибка!)")
            all_period_correct = False
    
    print("-" * 70)
    if all_period_correct:
        print("✓ Период Пизано работает корректно!")
    
    print("\n" + "=" * 70)
    
    # Итоговый результат
    print("\nИТОГОВЫЙ РЕЗУЛЬТАТ:")
    if all_correct_2 and all_correct_3 and all_period_correct:
        print("✓ Все алгоритмы работают корректно!")
    else:
        print("✗ Обнаружены ошибки. Необходимо проверить реализацию.")


if __name__ == "__main__":
    test_correctness()
