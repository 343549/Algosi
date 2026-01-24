"""
Задача 1: Рогалик (Roguelike)
Путешественник должен пройти из левого верхнего угла в правый нижний угол,
собирая максимальное количество монет. Может двигаться только вправо (R) или вниз (D).
"""

def solve_roguelike(input_file, output_file):
    # Читаем входной файл
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Парсим CSV файл
    grid = []
    for line in lines:
        line = line.strip()
        if line:
            row = [int(x.strip()) for x in line.split(';')]
            grid.append(row)
    
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    
    # Динамическое программирование: dp[i][j] = максимальное количество монет до клетки (i, j)
    dp = [[0] * m for _ in range(n)]
    path = [[''] * m for _ in range(n)]
    
    # Инициализация начальной клетки
    dp[0][0] = grid[0][0]
    
    # Заполняем первую строку (можно двигаться только вправо)
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
        path[0][j] = path[0][j-1] + 'R'
    
    # Заполняем первый столбец (можно двигаться только вниз)
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        path[i][0] = path[i-1][0] + 'D'
    
    # Заполняем остальные клетки
    for i in range(1, n):
        for j in range(1, m):
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j] + grid[i][j]
                path[i][j] = path[i-1][j] + 'D'
            else:
                dp[i][j] = dp[i][j-1] + grid[i][j]
                path[i][j] = path[i][j-1] + 'R'
    
    # Записываем результат
    max_coins = dp[n-1][m-1]
    best_path = path[n-1][m-1]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{max_coins}\n")
        f.write(best_path)
    
    return max_coins, best_path


if __name__ == "__main__":
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    max_coins, path = solve_roguelike('roguelike-input.csv', 'roguelike-output.txt')
    print(f"Максимальное количество монет: {max_coins}")
    print(f"Путь: {path}")
