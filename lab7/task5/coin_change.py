"""
Задача 5: Размен монет
Найти минимальное количество монет для размена заданной суммы.
"""

def coin_change(coins, amount):
    """
    Находит минимальное количество монет для размена суммы amount.
    coins - список номиналов монет
    amount - сумма для размена
    Возвращает минимальное количество монет или -1, если размен невозможен.
    """
    # dp[i] = минимальное количество монет для размена суммы i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Для суммы 0 нужно 0 монет
    
    # Заполняем таблицу динамического программирования
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_with_way(coins, amount):
    """
    Находит минимальное количество монет и сам способ размена.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)  # Для восстановления пути
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    if dp[amount] == float('inf'):
        return -1, []
    
    # Восстанавливаем способ размена
    way = []
    current = amount
    while current > 0:
        coin = parent[current]
        way.append(coin)
        current -= coin
    
    return dp[amount], way


def solve_coin_change(input_file):
    """
    Читает входной файл и решает задачу размена монет.
    Формат входного файла:
    Первая строка: n (количество номиналов монет)
    Вторая строка: n номиналов монет
    Третья строка: amount (сумма для размена)
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    n = int(lines[0].strip())
    coins = list(map(int, lines[1].strip().split()))
    amount = int(lines[2].strip())
    
    min_coins, way = coin_change_with_way(coins, amount)
    
    if min_coins == -1:
        print(f"Невозможно разменять сумму {amount} данными монетами")
    else:
        print(f"Минимальное количество монет: {min_coins}")
        print(f"Способ размена: {way}")
        print(f"Использованные монеты: {sorted(way, reverse=True)}")
    
    return min_coins, way


if __name__ == "__main__":
    solve_coin_change('coin-change-input.txt')
