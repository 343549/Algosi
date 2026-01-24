"""
Задача 9: Распечатка
Динамическое программирование для нахождения минимальной стоимости печати.
"""

def solve(n, prices):
    """
    Находит минимальную стоимость печати n листов.
    prices = [A1, A2, A3, A4, A5, A6, A7] - цены за 1, 10, 100, 1000, 10000, 100000, 1000000 листов
    """
    # dp[i] - минимальная стоимость печати i листов
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # Размеры партий
    sizes = [1, 10, 100, 1000, 10000, 100000, 1000000]
    
    # Заполняем dp
    for i in range(1, n + 1):
        # Можем заказать любую партию, если она не превышает нужное количество
        for j in range(len(sizes)):
            size = sizes[j]
            price = prices[j]
            
            # Если можем заказать партию этого размера
            if size <= i:
                dp[i] = min(dp[i], dp[i - size] + price)
            else:
                # Можем заказать партию большего размера (если это выгоднее)
                dp[i] = min(dp[i], price)
    
    return dp[n]

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        prices = []
        for i in range(1, 8):
            prices.append(int(lines[i].strip()))
    
    # Решение задачи
    result = solve(n, prices)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(str(result) + '\n')
    
    # Вывод для отчета
    print(f"Input: n = {n}")
    print(f"Prices: {prices}")
    print(f"Minimum cost: {result}")

if __name__ == '__main__':
    main()
