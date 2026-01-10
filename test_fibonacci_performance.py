"""Тестирование производительности алгоритма вычисления чисел Фибоначчи (Задание 2).

Измеряет время выполнения алгоритма для различных значений n.
Также можно измерить объем используемой памяти.
"""

import time
import sys
import io

# Настройка вывода для поддержки UTF-8 в Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def calc_fib(n: int) -> int:
    """Вычисляет n-е число Фибоначчи (из задания 2)."""
    if n <= 1:
        return n
    
    prev_prev = 0
    prev = 1
    
    for i in range(2, n + 1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current
    
    return prev


def test_performance():
    """Тестирует производительность алгоритма для различных значений n."""
    
    # Тестовые значения: малые, средние, большие
    test_cases = [
        (0, "малое"),
        (1, "малое"),
        (5, "малое"),
        (10, "малое"),
        (20, "среднее"),
        (30, "среднее"),
        (40, "большое"),
        (45, "большое (максимальное)"),
    ]
    
    print("=" * 70)
    print("ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ: Задание 2 (Число Фибоначчи)")
    print("=" * 70)
    print(f"{'n':<5} {'Категория':<20} {'Результат':<25} {'Время (сек)':<15}")
    print("-" * 70)
    
    results = []
    
    for n, category in test_cases:
        # Измеряем время выполнения
        t_start = time.perf_counter()
        result = calc_fib(n)
        t_end = time.perf_counter()
        elapsed_time = t_end - t_start
        
        results.append((n, category, result, elapsed_time))
        
        # Форматируем вывод
        result_str = str(result)
        if len(result_str) > 20:
            result_str = result_str[:17] + "..."
        
        print(f"{n:<5} {category:<20} {result_str:<25} {elapsed_time:.9f}")
    
    print("-" * 70)
    
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
    
    # Проверяем, нет ли резкого увеличения времени для больших значений
    small_times = [r[3] for r in results if r[1] == "малое"]
    large_times = [r[3] for r in results if r[1] == "большое"]
    
    if small_times and large_times:
        avg_small = sum(small_times) / len(small_times)
        avg_large = sum(large_times) / len(large_times)
        
        if avg_small > 0:
            ratio = avg_large / avg_small
            print(f"Соотношение времени (большие/малые): {ratio:.2f}x")
            
            if ratio > 100:
                print("⚠️  ВНИМАНИЕ: Значительное увеличение времени для больших значений!")
                print("   Возможно, проблема со сложностью алгоритма.")
            else:
                print("✓ Время увеличивается ожидаемо (линейно с n)")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    test_performance()
