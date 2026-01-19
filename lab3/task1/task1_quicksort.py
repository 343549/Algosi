"""
Задача 1: Улучшение Quick sort
Вариант 19
Студент: Джафари Хоссаин
"""

import random
import time


def partition(arr, left, right):
    """
    Обычная процедура разделения (Partition) - страница 8
    Разделяет массив на две части: элементы меньше опорного и элементы больше опорного
    Использует первый элемент (A[l]) как опорный (Lomuto partition scheme)
    """
    # Выбираем первый элемент как опорный (согласно странице 8)
    pivot = arr[left]  # x = A[l]
    j = left  # j = l
    
    # Проходим от l+1 до r
    for i in range(left + 1, right + 1):  # for i = l + 1 to r
        if arr[i] <= pivot:  # if A[i] <= x
            j = j + 1
            arr[j], arr[i] = arr[i], arr[j]  # swap(A[j], A[i])
    
    # Перемещаем опорный элемент на правильное место
    arr[left], arr[j] = arr[j], arr[left]  # swap(A[l], A[j])
    return j  # return j


def randomized_partition(arr, left, right):
    """
    Рандомизированная версия partition - страница 12
    Выбираем случайный элемент и меняем его с первым (A[l])
    """
    # Выбираем случайный индекс от left до right
    random_index = random.randint(left, right)  # k = random(l, r)
    # Меняем первый элемент со случайным
    arr[left], arr[random_index] = arr[random_index], arr[left]  # swap(A[l], A[k])
    # Вызываем Partition, который ожидает pivot в A[l]
    return partition(arr, left, right)  # m = Partition(A, l, r)


def quicksort(arr, left, right):
    """Обычная быстрая сортировка"""
    if left < right:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)


def randomized_quicksort(arr, left, right):
    """
    Рандомизированная быстрая сортировка - страница 12
    Randomized-QuickSort(A, l, r)
    """
    if left < right:  # if l < r
        # k = random(l, r); swap(A[l], A[k]) - делается в randomized_partition
        pivot_index = randomized_partition(arr, left, right)  # m = Partition(A, l, r)
        randomized_quicksort(arr, left, pivot_index - 1)  # Randomized-QuickSort(A, l, m - 1)
        randomized_quicksort(arr, pivot_index + 1, right)  # Randomized-QuickSort(A, m + 1, r)


def partition3(arr, left, right):
    """
    Трёхстороннее разделение (Partition3) - алгоритм Dutch National Flag
    Разделяет массив на три части: < pivot, = pivot, > pivot
    Возвращает индексы m1 и m2, где:
    - arr[k] < pivot для left <= k < m1
    - arr[k] = pivot для m1 <= k <= m2
    - arr[k] > pivot для m2 < k <= right
    
    Использует первый элемент как pivot (для согласованности с основной Partition)
    """
    # Выбираем первый элемент как опорный
    pivot = arr[left]
    
    # Используем алгоритм Dutch National Flag
    # i - граница элементов < pivot (последний элемент < pivot)
    # j - текущий элемент
    # k - граница элементов > pivot (первый элемент > pivot)
    i = left  # Начинаем с left, так как left содержит pivot
    j = left + 1
    k = right + 1
    
    while j < k:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        elif arr[j] == pivot:
            j += 1
        else:  # arr[j] > pivot
            k -= 1
            arr[j], arr[k] = arr[k], arr[j]
    
    # Перемещаем pivot на правильное место
    # После цикла: элементы [left+1..i] < pivot, элементы [i+1..j-1] = pivot (если есть)
    # Нужно поменять left (pivot) с последним элементом < pivot (arr[i])
    arr[left], arr[i] = arr[i], arr[left]
    
    # Теперь структура: [< pivot][pivot][= pivot][> pivot]
    # Нужно переместить все = pivot после первого pivot
    # i теперь указывает на первый pivot
    m1 = i  # Начало элементов = pivot
    m2 = i  # Пока только один элемент = pivot
    
    # Перемещаем все элементы = pivot после первого pivot
    j = i + 1
    while j < k:
        if arr[j] == pivot:
            m2 += 1
            arr[m2], arr[j] = arr[j], arr[m2]
        j += 1
    
    return m1, m2


def randomized_partition3(arr, left, right):
    """
    Рандомизированная версия partition3
    Выбираем случайный элемент и меняем его с первым (A[l])
    """
    random_index = random.randint(left, right)
    arr[left], arr[random_index] = arr[random_index], arr[left]
    return partition3(arr, left, right)


def randomized_quicksort3(arr, left, right):
    """Рандомизированная быстрая сортировка с трёхсторонним разделением"""
    if left < right:
        m1, m2 = randomized_partition3(arr, left, right)
        randomized_quicksort3(arr, left, m1 - 1)
        randomized_quicksort3(arr, m2 + 1, right)


def merge_sort(arr):
    """Сортировка слиянием для сравнения"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """Слияние двух отсортированных массивов"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def read_input(filename):
    """Чтение входных данных"""
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))
    return n, arr


def write_output(filename, arr):
    """Запись выходных данных"""
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, arr)) + '\n')


def main():
    # Чтение входных данных
    n, arr = read_input('input.txt')
    
    # Создаём копии для разных алгоритмов
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()
    
    # Randomized QuickSort с обычным Partition
    start = time.time()
    randomized_quicksort(arr1, 0, n - 1)
    time1 = time.time() - start
    
    # Randomized QuickSort с Partition3
    start = time.time()
    randomized_quicksort3(arr2, 0, n - 1)
    time2 = time.time() - start
    
    # Merge Sort
    start = time.time()
    arr3 = merge_sort(arr3)
    time3 = time.time() - start
    
    # Записываем результат
    write_output('output.txt', arr1)
    
    print(f"Randomized QuickSort (Partition): {time1:.6f} сек")
    print(f"Randomized QuickSort (Partition3): {time2:.6f} сек")
    print(f"Merge Sort: {time3:.6f} сек")
    print(f"Результат записан в output.txt")


if __name__ == '__main__':
    main()
