"""
Задача 16: Продавец (TSP - Traveling Salesman Problem)
Динамическое программирование для нахождения кратчайшего пути коммивояжера.
"""

def solve_tsp(n, distances):
    """
    Решает задачу коммивояжера методом динамического программирования.
    """
    # dp[mask][last] - минимальная стоимость посетить все города в mask,
    # закончив в городе last
    INF = float('inf')
    dp = {}
    
    # Базовый случай: начинаем с города 0
    dp[(1, 0)] = 0
    
    # Перебираем все возможные маски
    for mask in range(1, 1 << n):
        for last in range(n):
            if not (mask & (1 << last)):
                continue
            
            state = (mask, last)
            if state not in dp:
                continue
            
            # Пробуем перейти в следующий город
            for next_city in range(n):
                if mask & (1 << next_city):
                    continue
                
                new_mask = mask | (1 << next_city)
                new_state = (new_mask, next_city)
                new_cost = dp[state] + distances[last][next_city]
                
                if new_state not in dp or dp[new_state] > new_cost:
                    dp[new_state] = new_cost
    
    # Находим минимальную стоимость вернуться в город 0
    full_mask = (1 << n) - 1
    min_cost = INF
    best_last = -1
    
    for last in range(1, n):
        state = (full_mask, last)
        if state in dp:
            cost = dp[state] + distances[last][0]
            if cost < min_cost:
                min_cost = cost
                best_last = last
    
    # Восстанавливаем путь
    path = []
    if best_last != -1:
        current_mask = full_mask
        current_city = best_last
        path.append(current_city)
        
        while current_mask != 1:  # Пока не остался только город 0
            for prev_city in range(n):
                if not (current_mask & (1 << prev_city)):
                    continue
                if prev_city == current_city:
                    continue
                
                prev_mask = current_mask ^ (1 << current_city)
                prev_state = (prev_mask, prev_city)
                
                if prev_state in dp:
                    if abs(dp[(current_mask, current_city)] - 
                           (dp[prev_state] + distances[prev_city][current_city])) < 1e-9:
                        current_mask = prev_mask
                        current_city = prev_city
                        path.append(current_city)
                        break
        
        path.append(0)
        path.reverse()
    
    return min_cost, path

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        distances = []
        for i in range(1, n + 1):
            distances.append(list(map(int, lines[i].strip().split())))
    
    # Решение задачи
    min_cost, path = solve_tsp(n, distances)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(str(min_cost) + '\n')
        # Нумерация городов с 1 для вывода (по условию задачи)
        path_1_indexed = [x + 1 for x in path]
        f.write(' '.join(map(str, path_1_indexed)) + '\n')
    
    # Вывод для отчета
    print(f"Input: n = {n}")
    print(f"Minimum cost: {min_cost}")
    print(f"Path (0-indexed): {path}")
    print(f"Path (1-indexed): {[x+1 for x in path]}")

if __name__ == '__main__':
    main()
