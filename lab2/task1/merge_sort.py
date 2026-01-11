def merge_sort(arr):
    """
    Реализация алгоритма сортировки слиянием (Merge Sort).
    Сортирует массив по возрастанию, используя принцип "разделяй и властвуй".
    """
    if len(arr) <= 1:
        return arr
    
    # Делим массив пополам
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Сливаем отсортированные половины
    return merge(left_half, right_half)


def merge(left, right):
    """
    Функция слияния двух отсортированных массивов в один отсортированный.
    """
    merged = []
    left_index = 0
    right_index = 0
    
    # Сравниваем элементы из обоих массивов и добавляем меньший
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Добавляем оставшиеся элементы
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged


if __name__ == "__main__":
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))
    
    # Сортировка
    sorted_arr = merge_sort(arr.copy())
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, sorted_arr)))
    
    # Вывод для отчёта
    print("Исходный массив:", arr)
    print("Отсортированный массив:", sorted_arr)
