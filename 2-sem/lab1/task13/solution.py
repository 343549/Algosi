"""
Задача 13: Сувениры
Динамическое программирование для проверки возможности разделения
сувениров на три равные части.
"""

def solve(n, values):
    """
    Проверяет, можно ли разбить сувениры на три подмножества с одинаковыми суммами.
    """
    total = sum(values)
    
    # Если сумма не делится на 3, невозможно
    if total % 3 != 0:
        return 0
    
    target = total // 3
    
    # Если есть элемент больше target, невозможно
    if any(v > target for v in values):
        return 0
    
    # dp[mask] = можно ли разбить элементы с маской mask на подмножества
    # Используем битовую маску для представления подмножеств
    # dp[mask][sum1][sum2] - можно ли разбить элементы mask так, 
    # чтобы первое подмножество имело сумму sum1, второе - sum2
    
    # Упрощенный подход: проверяем все возможные разбиения
    from itertools import combinations
    
    # Перебираем все возможные подмножества для первого и второго набора
    all_subsets = []
    for r in range(1, n):
        for combo in combinations(range(n), r):
            subset_sum = sum(values[i] for i in combo)
            if subset_sum == target:
                all_subsets.append(set(combo))
    
    # Проверяем, есть ли два непересекающихся подмножества с суммой target
    for i, subset1 in enumerate(all_subsets):
        for subset2 in all_subsets[i+1:]:
            if subset1.isdisjoint(subset2):
                # Нашли два непересекающихся подмножества
                # Третье автоматически будет иметь нужную сумму
                return 1
    
    return 0

def solve_dp(n, values):
    """
    Решение через динамическое программирование.
    """
    total = sum(values)
    
    if total % 3 != 0:
        return 0
    
    target = total // 3
    
    if any(v > target for v in values):
        return 0
    
    # dp[mask] = множество возможных пар (sum1, sum2) для маски mask
    # где sum1 - сумма первого подмножества, sum2 - второго
    dp = {}
    dp[0] = {(0, 0)}
    
    for mask in range(1, 1 << n):
        dp[mask] = set()
        # Находим последний добавленный элемент
        for i in range(n):
            if mask & (1 << i):
                prev_mask = mask ^ (1 << i)
                if prev_mask in dp:
                    for sum1, sum2 in dp[prev_mask]:
                        # Добавляем элемент i в первое подмножество
                        new_sum1 = sum1 + values[i]
                        if new_sum1 <= target:
                            dp[mask].add((new_sum1, sum2))
                        
                        # Добавляем элемент i во второе подмножество
                        new_sum2 = sum2 + values[i]
                        if new_sum2 <= target:
                            dp[mask].add((sum1, new_sum2))
        
        # Проверяем, достигли ли цели
        if (target, target) in dp[mask]:
            return 1
    
    return 0

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        values = list(map(int, lines[1].strip().split()))
    
    # Решение задачи
    result = solve_dp(n, values)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(str(result) + '\n')
    
    # Вывод для отчета
    print(f"Input: n = {n}, values = {values}")
    print(f"Total sum: {sum(values)}")
    print(f"Target per subset: {sum(values) // 3 if sum(values) % 3 == 0 else 'N/A'}")
    print(f"Result: {result}")

if __name__ == '__main__':
    main()
