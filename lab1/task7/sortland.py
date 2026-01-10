"""
Задача №7. Знакомство с жителями Сортлэнда
Владелец графства Сортлэнд, граф Бабблсортер, решил познакомиться со своими подданными.
Число жителей в графстве нечетно и составляет n, где n может быть достаточно велико,
поэтому граф решил ограничиться знакомством с тремя представителями народонаселения:
с самым бедным жителем, с жителем, обладающим средним достатком, и с самым богатым жителем.
"""


def find_residents(wealth_array):
    """
    Находит идентификационные номера беднейшего, среднего и богатейшего жителей.
    
    Args:
        wealth_array: список вещественных чисел, представляющих достаток жителей
        
    Returns:
        tuple: (беднейший_id, средний_id, богатейший_id)
    """
    n = len(wealth_array)
    
    # Создаем список пар (достаток, идентификационный номер)
    # Индексация начинается с 1, поэтому используем i+1
    wealth_with_id = [(wealth_array[i], i + 1) for i in range(n)]
    
    # Сортируем по достатку (по возрастанию)
    wealth_with_id.sort(key=lambda x: x[0])
    
    # Определяем идентификационные номера
    poorest_id = wealth_with_id[0][1]      # Первый в отсортированном списке (самый бедный)
    middle_id = wealth_with_id[n // 2][1]  # Средний элемент (n нечетно, поэтому n//2 - центральный)
    richest_id = wealth_with_id[-1][1]     # Последний в отсортированном списке (самый богатый)
    
    return poorest_id, middle_id, richest_id


if __name__ == "__main__":
    # Чтение входных данных из файла
    with open("task7/input.txt", "r", encoding="utf-8") as input_file:
        n = int(input_file.readline().strip())
        money = list(map(float, input_file.readline().split()))
    
    # Проверка корректности данных
    if len(money) != n:
        print(f"Error: expected {n} elements, got {len(money)}")
        exit(1)
    
    if n % 2 == 0:
        print("Warning: n should be odd according to the task conditions")
    
    print(f"Number of residents: {n}")
    print(f"Residents' wealth: {money}")
    
    # Поиск требуемых жителей
    poorest_id, middle_id, richest_id = find_residents(money)
    
    print(f"\nResults:")
    print(f"Poorest resident (ID): {poorest_id}")
    print(f"Middle resident (ID): {middle_id}")
    print(f"Richest resident (ID): {richest_id}")
    
    # Демонстрация процесса сортировки
    wealth_with_id = [(money[i], i + 1) for i in range(n)]
    wealth_with_id.sort(key=lambda x: x[0])
    print(f"\nSorted list of residents by wealth:")
    for wealth, resident_id in wealth_with_id:
        print(f"  [${wealth:.2f}, ID={resident_id}]")
    
    # Запись результата в выходной файл
    with open("task7/output.txt", "w", encoding="utf-8") as output_file:
        output_file.write(f"{poorest_id} {middle_id} {richest_id}")
    
    print(f"\nResult written to output.txt: {poorest_id} {middle_id} {richest_id}")
