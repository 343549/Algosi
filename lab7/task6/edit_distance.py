"""
Задача 6: Редакционное расстояние (расстояние Левенштейна)
Найти минимальное количество операций (вставка, удаление, замена) для преобразования
одной строки в другую.
"""

def edit_distance(s1, s2):
    """
    Вычисляет редакционное расстояние между двумя строками.
    Возвращает минимальное количество операций и последовательность операций.
    """
    n = len(s1)
    m = len(s2)
    
    # dp[i][j] = минимальное расстояние между s1[0:i] и s2[0:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Инициализация: расстояние от пустой строки
    for i in range(n + 1):
        dp[i][0] = i  # Удалить i символов
    for j in range(m + 1):
        dp[0][j] = j  # Вставить j символов
    
    # Заполняем таблицу
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                # Символы совпадают, операция не нужна
                dp[i][j] = dp[i-1][j-1]
            else:
                # Выбираем минимальную из трех операций:
                # 1. Замена: dp[i-1][j-1] + 1
                # 2. Удаление: dp[i-1][j] + 1
                # 3. Вставка: dp[i][j-1] + 1
                dp[i][j] = min(
                    dp[i-1][j-1] + 1,  # Замена
                    dp[i-1][j] + 1,     # Удаление
                    dp[i][j-1] + 1      # Вставка
                )
    
    # Восстанавливаем последовательность операций
    operations = []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
            # Символы совпадают, переходим дальше
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + 1:
            # Замена
            operations.append(f"Заменить '{s1[i-1]}' на '{s2[j-1]}' в позиции {i-1}")
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            # Удаление
            operations.append(f"Удалить '{s1[i-1]}' в позиции {i-1}")
            i -= 1
        else:
            # Вставка
            operations.append(f"Вставить '{s2[j-1]}' в позицию {i}")
            j -= 1
    
    operations.reverse()
    return dp[n][m], operations


def solve_edit_distance(input_file):
    """
    Читает входной файл и вычисляет редакционное расстояние.
    Формат входного файла:
    Первая строка: первая строка
    Вторая строка: вторая строка
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    s1 = lines[0].strip()
    s2 = lines[1].strip()
    
    distance, operations = edit_distance(s1, s2)
    
    print(f"Редакционное расстояние: {distance}")
    print(f"Количество операций: {distance}")
    print("\nПоследовательность операций:")
    for i, op in enumerate(operations, 1):
        print(f"{i}. {op}")
    
    return distance, operations


if __name__ == "__main__":
    solve_edit_distance('edit-distance-input.txt')
