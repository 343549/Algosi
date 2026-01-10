"""Тестирование производительности алгоритма вычисления последней цифры (Задание 3).

Измеряет время выполнения алгоритма для различных значений n (включая очень большие).
Также можно измерить объем используемой памяти.
"""

import time
import sys
import io

# Настройка вывода для поддержки UTF-8 в Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def calc_fib_last_digit(n: int) -> int:
    """Вычисляет последнюю цифру n-го числа Фибоначчи (из задания 3)."""
    if n <= 1:
        return n
    
    # Используем период Пизано (60 для последней цифры)
    n_mod_period = n % 60
    
    prev_prev = 0
    prev = 1
    
    for i in range(2, n_mod_period + 1):
        current = (prev_prev + prev) % 10
        prev_prev = prev
        prev = current
    
    return prev


def test_performance():
    """Тестирует производительность алгоритма для различных значений n."""
    
    # Тестовые значения: малые, средние, большие, очень большие
    test_cases = [
        (0, "малое"),
        (1, "малое"),
        (5, "малое"),
        (10, "малое"),
        (45, "малое"),
        (100, "среднее"),
        (1000, "среднее"),
        (10000, "большое"),
        (100000, "большое"),
        (1000000, "очень большое"),
        (5000000, "очень большое"),
        (10000000, "очень большое (максимальное)"),
    ]
    
    print("=" * 80)
    print("ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ: Задание 3 (Последняя цифра Фибоначчи)")
    print("=" * 80)
    print(f"{'n':<12} {'Категория':<20} {'Результат':<10} {'Время (сек)':<15} {'n mod 60':<10}")
    print("-" * 80)
    
    results = []
    
    for n, category in test_cases:
        # Измеряем время выполнения
        t_start = time.perf_counter()
        result = calc_fib_last_digit(n)
        t_end = time.perf_counter()
        elapsed_time = t_end - t_start
        n_mod = n % 60
        
        results.append((n, category, result, elapsed_time, n_mod))
        
        print(f"{n:<12} {category:<20} {result:<10} {elapsed_time:.9f} {n_mod:<10}")
    
    print("-" * 80)
    
    # Анализ результатов
    print("\nАНАЛИЗ РЕЗУЛЬТАТОВ:")
    print(f"Всего протестировано значений: {len(test_cases)}")
    
    min_time = min(r[3] for r in results)
    max_time = max(r[3] for r in results)
    avg_time = sum(r[3] for r in results) / len(results)
    
    print(f"Минимальное время выполнения: {min_time:.9f} сек")
    print(f"Максимальное время выполнения: {max_time:.9f} сек")
    print(f"Среднее время выполнения: {avg_time:.9f} сек")
    
    # Проверка на проблемы с производительностью
    print("\nПРОВЕРКА НА ПРОБЛЕМЫ:")
    
    # Проверяем, что время примерно константное (благодаря периоду Пизано)
    small_times = [r[3] for r in results if r[1] == "малое"]
    very_large_times = [r[3] for r in results if r[1] == "очень большое"]
    
    if small_times and very_large_times:
        avg_small = sum(small_times) / len(small_times)
        avg_very_large = sum(very_large_times) / len(very_large_times)
        
        if avg_small > 0:
            ratio = avg_very_large / avg_small
            print(f"Соотношение времени (очень большие/малые): {ratio:.2f}x")
            
            if ratio < 2:
                print("✓ Отлично! Время выполнения примерно константное (O(1))")
                print("  Период Пизано работает эффективно!")
            elif ratio < 5:
                print("✓ Хорошо! Время увеличивается незначительно")
            else:
                print("⚠️  ВНИМАНИЕ: Время значительно увеличивается")
                print("   Возможно, проблема с реализацией периода Пизано")
    
    # Проверяем, что n mod 60 корректно работает
    print("\nПРОВЕРКА КОРРЕКТНОСТИ:")
    print("Проверяем, что для больших n результат зависит только от n mod 60...")
    
    # Тест: n и n + 60 должны давать одинаковую последнюю цифру
    test_pairs = [(100, 160), (1000, 1060), (10000, 10060)]
    all_correct = True
    
    for n1, n2 in test_pairs:
        result1 = calc_fib_last_digit(n1)
        result2 = calc_fib_last_digit(n2)
        if result1 == result2:
            print(f"✓ F({n1}) mod 10 = F({n2}) mod 10 = {result1} (корректно)")
        else:
            print(f"✗ F({n1}) mod 10 = {result1}, F({n2}) mod 10 = {result2} (ошибка!)")
            all_correct = False
    
    if all_correct:
        print("Все проверки периода Пизано пройдены успешно!")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    test_performance()
