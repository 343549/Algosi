"""
Задача №1. Сортировка вставкой
Используя код процедуры Insertion-sort, напишите программу и проверьте сортировку массива A = {31, 41, 59, 26, 41, 58}.
"""

def insertion_sort(arr):
    """
    Реализация алгоритма сортировки вставкой.
    Сортирует массив по возрастанию.
    """
    if len(arr) <= 1:
        return arr
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


def run_test(input_data):
    """
    Функция для тестирования алгоритма на заданных данных.
    """
    lines = input_data.strip().split("\n")
    lines = [item for item in lines if item.strip() != ""]
    
    if len(lines) < 2:
        return "\033[91mОшибка: неверный формат теста\033[00m"
    
    try:
        n = int(lines[0].strip())
        array = list(map(int, lines[1].split()))
        
        if len(array) != n:
            return f"\033[91mОшибка: ожидание {n} элемента, но {len(array)} элемент получен\033[00m"
        
        insertion_sort(array)
        return " ".join(map(str, array))
    except ValueError as e:
        return f"\033[91mОшибка: {e}\033[00m"


def run_tests_from_file():
    """
    Чтение и выполнение тестов из файла "tests.txt"
    """
    try:
        with open("task1/tests.txt", "r", encoding="utf-8") as test_file:
            test_data = test_file.read()
        
        tests = test_data.split("\n\n")
        for i, test in enumerate(tests):
            if not test.strip():
                continue
            result = run_test(test)
            print(f"Test {i + 1}\t: {result}")
    except FileNotFoundError:
        print("\033[91mФайл tests.txt не найден\033[00m")


if __name__ == "__main__":
    # Основная работа программы
    with open("task1/input.txt", "r", encoding="utf-8") as input_file:
        n = int(input_file.readline().strip())
        array = list(map(int, input_file.readline().split()))
    
    print(f"Array before sorting: {array}")
    
    insertion_sort(array)
    
    print(f"Array after sorting: {array}")
    
    with open("task1/output.txt", "w", encoding="utf-8") as output_file:
        output_file.write(" ".join(map(str, array)))
    
    print("\nAdditional tests:")
    run_tests_from_file()
