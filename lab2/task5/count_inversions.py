def merge_and_count(left, right):
    """
    Функция слияния двух отсортированных массивов с подсчётом инверсий.
    Инверсия возникает, когда элемент из правого массива меньше элемента из левого.
    """
    merged = []
    inversions = 0
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            # Все оставшиеся элементы в left больше текущего элемента right
            inversions += len(left) - left_index
            right_index += 1
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged, inversions


def count_inversions_merge_sort(arr):
    """
    Подсчёт количества инверсий в массиве с помощью сортировки слиянием.
    Инверсия - это пара индексов (i, j), где i < j и arr[i] > arr[j].
    """
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left_arr, left_inversions = count_inversions_merge_sort(arr[:mid])
    right_arr, right_inversions = count_inversions_merge_sort(arr[mid:])
    
    merged, merge_inversions = merge_and_count(left_arr, right_arr)
    total_inversions = left_inversions + right_inversions + merge_inversions
    
    return merged, total_inversions


if __name__ == "__main__":
    # Тестовый массив
    test_array = [38, 27, 43, 3, 9, 82, 10, 16]
    
    print("=" * 60)
    print("Задача 5: Подсчёт инверсий с помощью Merge Sort")
    print("=" * 60)
    print(f"Исходный массив: {test_array}")
    
    sorted_arr, inversions = count_inversions_merge_sort(test_array.copy())
    
    print(f"Отсортированный массив: {sorted_arr}")
    print(f"Количество инверсий: {inversions}")
    print("=" * 60)
    
    # Дополнительные тесты
    print("\nДополнительные примеры:")
    print("-" * 60)
    
    test_cases = [
        [2, 4, 1, 3, 5],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [1, 3, 2],
    ]
    
    for test in test_cases:
        _, inv = count_inversions_merge_sort(test.copy())
        print(f"Массив {test}: {inv} инверсий")
