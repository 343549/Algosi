def merge(arr, left, mid, right):
    """
    Функция слияния двух отсортированных подмассивов arr[left..mid] и arr[mid+1..right].
    Работает in-place, используя вспомогательный массив.
    """
    # Создаём временные массивы для левой и правой частей
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    # Сливаем временные массивы обратно в arr[left..right]
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Копируем оставшиеся элементы
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def iterative_merge_sort(arr):
    """
    Итеративная версия сортировки слиянием.
    Вместо рекурсии использует циклы для объединения подмассивов.
    """
    n = len(arr)
    # Начинаем с подмассивов размером 1, затем увеличиваем размер
    current_size = 1
    
    while current_size < n:
        left = 0
        while left < n - 1:
            # Находим конец первого подмассива
            mid = min(left + current_size - 1, n - 1)
            
            # Находим конец второго подмассива
            right = min(left + 2 * current_size - 1, n - 1)
            
            # Сливаем подмассивы arr[left..mid] и arr[mid+1..right]
            if mid < right:
                merge(arr, left, mid, right)
            
            left += 2 * current_size
        
        # Увеличиваем размер подмассивов в два раза
        current_size *= 2
    
    return arr


if __name__ == "__main__":
    # Тестовый массив
    test_array = [38, 27, 43, 3, 9, 82, 10, 16]
    
    print("=" * 60)
    print("Задача 7: Итеративная версия Merge Sort")
    print("=" * 60)
    print(f"Исходный массив: {test_array}")
    
    sorted_arr = iterative_merge_sort(test_array.copy())
    
    print(f"Отсортированный массив: {sorted_arr}")
    print("=" * 60)
    
    # Дополнительные тесты
    print("\nДополнительные примеры:")
    print("-" * 60)
    
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
    ]
    
    for test in test_cases:
        if test:  # Проверяем, что массив не пустой
            original = test.copy()
            sorted_test = iterative_merge_sort(test.copy())
            print(f"Исходный: {original} -> Отсортированный: {sorted_test}")
        else:
            sorted_test = iterative_merge_sort(test.copy())
            print(f"Пустой массив -> Отсортированный: {sorted_test}")
