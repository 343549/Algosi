"""
Задача 5: Максимальное количество призов
Жадный алгоритм для представления числа n в виде суммы максимального количества
попарно различных натуральных чисел.
"""

def solve(n):
    """
    Находит максимальное количество попарно различных натуральных чисел,
    сумма которых равна n.
    """
    result = []
    current = 1
    remaining = n
    
    # Жадный алгоритм: берем наименьшие числа, начиная с 1
    while remaining >= current:
        result.append(current)
        remaining -= current
        current += 1
    
    # Если остался остаток, добавляем его к последнему числу
    if remaining > 0:
        result[-1] += remaining
    
    return result

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        n = int(f.read().strip())
    
    # Решение задачи
    result = solve(n)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(str(len(result)) + '\n')
        f.write(' '.join(map(str, result)) + '\n')
    
    # Вывод для отчета
    print(f"Input: n = {n}")
    print(f"Maximum number of prizes: {len(result)}")
    print(f"Distribution: {result}")
    print(f"Sum check: {sum(result)} = {n}")

if __name__ == '__main__':
    main()
