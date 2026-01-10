"""
Задача №5. Сортировка выбором.
Рассмотрим сортировку элементов массива, которая выполняется следующим образом. 
Сначала определяется наименьший элемент массива, который ставится на место элемента A[1]. 
Затем производится поиск второго наименьшего элемента массива A, который ставится на место элемента A[2]. 
Этот процесс продолжается для первых n − 1 элементов массива A.
"""

import time


def selection_sort(array):
    """
    Реализация алгоритма сортировки выбором.
    Находит минимальный элемент на каждой итерации и ставит его на правильную позицию.
    """
    n = len(array)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


def test_sorting_time(array, description):
    """
    Тестирование времени сортировки на заданном массиве.
    """
    arr_copy = array.copy()
    print(f"\n{description}:")
    print(f"Array before sorting: {arr_copy[:20]}{'...' if len(arr_copy) > 20 else ''}")
    
    start = time.time()
    selection_sort(arr_copy)
    end = time.time()
    
    print(f"Array after sorting: {arr_copy[:20]}{'...' if len(arr_copy) > 20 else ''}")
    print(f"Sorting time: {(end - start):.6f} seconds")
    return end - start


if __name__ == "__main__":
    # Чтение входных данных
    with open("task5/input.txt", "r", encoding="utf-8") as in_file:
        n = int(in_file.readline().strip())
        array = list(map(int, in_file.readline().split()))
    
    print("=" * 60)
    print("SELECTION SORT")
    print("=" * 60)
    
    # Основная сортировка
    print(f"\nOriginal array ({n} elements): {array}")
    
    start = time.time()
    sorted_array = selection_sort(array.copy())
    end = time.time()
    
    print(f"Sorted array: {sorted_array}")
    print(f"Sorting time: {(end - start):.6f} seconds")
    
    # Запись результата в файл
    with open("task5/output.txt", "w", encoding="utf-8") as out_file:
        out_file.write(" ".join(map(str, sorted_array)))
    
    # Тестирование в наихудшем случае (обратный порядок)
    worst_case = list(range(100, 0, -1))
    worst_time = test_sorting_time(worst_case, "Worst case (reverse order, 100 elements)")
    
    # Тестирование в среднем случае (случайный порядок)
    import random
    random.seed(42)
    average_case = [random.randint(1, 1000) for _ in range(100)]
    average_time = test_sorting_time(average_case, "Average case (random order, 100 elements)")
    
    print("\n" + "=" * 60)
    print("COMPARISON: SELECTION SORT vs INSERTION SORT")
    print("=" * 60)
    print("""
Selection Sort:
- Time complexity: O(n²) in worst, average, and best cases
- Number of comparisons: always n(n-1)/2
- Number of swaps: n-1 (minimum possible)
- Feature: independent of initial element order

Insertion Sort:
- Time complexity: O(n²) in worst and average cases, O(n) in best case
- Number of comparisons: from n-1 (best case) to n(n-1)/2 (worst case)
- Number of swaps: from 0 to n(n-1)/2
- Feature: efficient on partially ordered arrays

Conclusion:
For small arrays both algorithms work quickly, but insertion sort can be more
efficient on partially ordered data, as in the best case it works in O(n).
Selection sort has constant complexity but requires minimum swaps, which can be
useful when working with expensive swap operations.
    """)
