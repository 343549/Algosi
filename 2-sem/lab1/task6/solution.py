"""
Задача 6: Максимальная зарплата
Жадный алгоритм для составления наибольшего числа из набора целых чисел.
"""

def compare(a, b):
    """
    Сравнивает два числа для сортировки.
    Возвращает True, если a должно идти перед b.
    """
    # Сравниваем конкатенации: ab vs ba
    return str(a) + str(b) > str(b) + str(a)

def solve(numbers):
    """
    Составляет наибольшее число из набора чисел.
    """
    # Сортируем числа по специальному компаратору
    # Используем пузырьковую сортировку для простоты
    n = len(numbers)
    arr = numbers[:]
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if not compare(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return ''.join(map(str, arr))

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        numbers = list(map(int, lines[1].strip().split()))
    
    # Решение задачи
    result = solve(numbers)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(result + '\n')
    
    # Вывод для отчета
    print(f"Input numbers: {numbers}")
    print(f"Maximum number: {result}")

if __name__ == '__main__':
    main()
