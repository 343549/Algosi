"""
Задача 3: Наибольшая общая подпоследовательность (НОП / LCS)
Найти наибольшую общую подпоследовательность двух последовательностей.
"""

def lcs(seq1, seq2):
    """
    Находит наибольшую общую подпоследовательность двух последовательностей.
    Возвращает длину и саму подпоследовательность.
    """
    n = len(seq1)
    m = len(seq2)
    
    # dp[i][j] = длина НОП для seq1[0:i] и seq2[0:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Заполняем таблицу динамического программирования
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Восстанавливаем подпоследовательность
    lcs_sequence = []
    i, j = n, m
    while i > 0 and j > 0:
        if seq1[i-1] == seq2[j-1]:
            lcs_sequence.append(seq1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    lcs_sequence.reverse()
    return dp[n][m], lcs_sequence


def solve_lcs(input_file):
    """
    Читает входной файл и находит НОП.
    Формат входного файла:
    Первая строка: n (длина первой последовательности)
    Вторая строка: n чисел первой последовательности
    Третья строка: m (длина второй последовательности)
    Четвертая строка: m чисел второй последовательности
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    n = int(lines[0].strip())
    seq1 = list(map(int, lines[1].strip().split()))
    m = int(lines[2].strip())
    seq2 = list(map(int, lines[3].strip().split()))
    
    length, sequence = lcs(seq1, seq2)
    
    print(f"Длина НОП: {length}")
    print(f"НОП: {' '.join(map(str, sequence))}")
    
    return length, sequence


if __name__ == "__main__":
    solve_lcs('lcs-input.txt')
