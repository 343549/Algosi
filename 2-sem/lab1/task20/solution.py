"""
Задача 20: Почти палиндром
Динамическое программирование для подсчета подслов, являющихся почти палиндромами.
"""

def is_almost_palindrome(s, k):
    """
    Проверяет, является ли строка s почти палиндромом с k изменениями.
    """
    n = len(s)
    # dp[i][j] - минимальное количество изменений для подстроки s[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    # Заполняем для подстрок длины 1 и 2
    for i in range(n):
        dp[i][i] = 0
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if i + 1 <= j - 1:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 0
            else:
                if i + 1 <= j - 1:
                    dp[i][j] = dp[i + 1][j - 1] + 1
                else:
                    dp[i][j] = 1
    
    return dp[0][n - 1] <= k

def solve(s, k):
    """
    Подсчитывает количество подслов, являющихся почти палиндромами.
    """
    n = len(s)
    count = 0
    
    # Перебираем все подслова
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if is_almost_palindrome(substring, k):
                count += 1
    
    return count

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n, k = map(int, lines[0].strip().split())
        s = lines[1].strip()
    
    # Решение задачи
    result = solve(s, k)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write(str(result) + '\n')
    
    # Вывод для отчета
    print(f"Input: n = {n}, k = {k}, s = '{s}'")
    print(f"Number of almost palindromes: {result}")

if __name__ == '__main__':
    main()
