def find_max_crossing_subarray(A, low, mid, high):
    """
    Находит максимальный подмассив, пересекающий среднюю точку.
    Основано на псевдокоде Find Max Crossing Subarray из Лекции 2 (страницы 25-26).
    
    Параметры:
    - A: массив элементов
    - low: начальный индекс (p в псевдокоде)
    - mid: средний индекс (q в псевдокоде)
    - high: конечный индекс (r в псевдокоде)
    
    Предполагается: low <= mid < high
    A[low..mid] и A[mid+1..high] - отсортированы (для контекста Merge Sort)
    Но для Maximum Subarray это не требуется - ищем максимальную сумму.
    
    Возвращает: (max_left, max_right, left_sum + right_sum)
    """
    # Левая часть: находим максимальную сумму, заканчивающуюся в mid
    # Соответствует псевдокоду: left_sum = -∞, sum = 0
    left_sum = float('-inf')  # -∞
    sum_val = 0
    max_left = mid
    
    # for i = mid downto low (в псевдокоде)
    for i in range(mid, low - 1, -1):
        sum_val = sum_val + A[i]  # sum = sum + A[i]
        if sum_val > left_sum:    # if sum > left_sum
            left_sum = sum_val    # then left_sum = sum
            max_left = i          # max_left = i
    
    # Правая часть: находим максимальную сумму, начинающуюся в mid+1
    # Соответствует псевдокоду: right_sum = -∞, sum = 0
    right_sum = float('-inf')  # -∞
    sum_val = 0
    max_right = mid + 1
    
    # for j = mid + 1 to high (в псевдокоде)
    for j in range(mid + 1, high + 1):
        sum_val = sum_val + A[j]  # sum = sum + A[j]
        if sum_val > right_sum:   # if sum > right_sum
            right_sum = sum_val    # then right_sum = sum
            max_right = j          # max_right = j
    
    # return (max_left, max_right, left_sum + right_sum)
    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(A, low, high):
    """
    Находит максимальный подмассив, используя метод "Разделяй и властвуй".
    Основано на псевдокоде Find Maximum Subarray из Лекции 2 (страницы 25-26).
    
    Параметры:
    - A: массив элементов
    - low: начальный индекс (p в псевдокоде)
    - high: конечный индекс (r в псевдокоде)
    
    Возвращает: (low_index, high_index, sum)
    """
    # Базовый случай: if high == low
    if high == low:
        return low, high, A[low]  # return (low, high, A[low])
    
    # else mid = ⌊(low + high) / 2⌋
    mid = (low + high) // 2
    
    # Рекурсивно находим максимальный подмассив в левой половине
    # (left_low, left_high, left_sum) = Find Maximum Subarray(A, low, mid)
    left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
    
    # Рекурсивно находим максимальный подмассив в правой половине
    # (right_low, right_high, right_sum) = Find Maximum Subarray(A, mid + 1, high)
    right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
    
    # Находим максимальный подмассив, пересекающий среднюю точку
    # (cross_low, cross_high, cross_sum) = Find Max Crossing Subarray(A, low, mid, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
    
    # Возвращаем подмассив с максимальной суммой
    # if left_sum >= right_sum and left_sum >= cross_sum
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    # elseif right_sum >= left_sum and right_sum >= cross_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    # else return (cross_low, cross_high, cross_sum)
    else:
        return cross_low, cross_high, cross_sum


def calculate_price_changes(prices):
    """
    Вычисляет изменения цен (разницы между соседними днями).
    Это необходимо для применения алгоритма Maximum Subarray.
    """
    changes = []
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i - 1])
    return changes


if __name__ == "__main__":
    # Пример с данными акций
    # Для демонстрации используем упрощённые данные
    # В реальном случае данные можно загрузить из файла или скачать с Google Finance
    
    print("=" * 60)
    print("Задача 6: Поиск максимальной прибыли")
    print("=" * 60)
    
    # Пример: цены акций за несколько дней
    # Формат: (день, цена)
    stock_data = [
        ("2024-01-01", 100),
        ("2024-01-02", 105),
        ("2024-01-03", 102),
        ("2024-01-04", 108),
        ("2024-01-05", 110),
        ("2024-01-06", 107),
        ("2024-01-07", 115),
        ("2024-01-08", 112),
    ]
    
    company_name = "Пример компании"
    period = "01.01.2024 - 08.01.2024"
    
    # Извлекаем цены
    prices = [price for _, price in stock_data]
    dates = [date for date, _ in stock_data]
    
    print(f"Компания: {company_name}")
    print(f"Период: {period}")
    print(f"\nЦены акций по дням:")
    for date, price in stock_data:
        print(f"  {date}: {price}")
    
    # Вычисляем изменения цен
    price_changes = calculate_price_changes(prices)
    print(f"\nИзменения цен (прибыль/убыток за день):")
    for i, change in enumerate(price_changes):
        print(f"  День {i+1}→{i+2}: {change:+}")
    
    # Находим максимальный подмассив (максимальную прибыль)
    if len(price_changes) > 0:
        buy_day_idx, sell_day_idx, max_profit = find_maximum_subarray(price_changes, 0, len(price_changes) - 1)
        
        # Индексы для дат: buy_day_idx соответствует дню покупки, sell_day_idx+1 - дню продажи
        buy_date = dates[buy_day_idx]
        sell_date = dates[sell_day_idx + 1]
        
        print(f"\n{'='*60}")
        print("РЕЗУЛЬТАТ:")
        print(f"{'='*60}")
        print(f"Дата покупки: {buy_date}")
        print(f"Дата продажи: {sell_date}")
        print(f"Максимальная прибыль: {max_profit}")
        print(f"{'='*60}")
        
        # Запись в файл
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(f"Компания: {company_name}\n")
            f.write(f"Период изменения цен акций: {period}\n")
            f.write(f"Дата покупки: {buy_date}\n")
            f.write(f"Дата продажи: {sell_date}\n")
            f.write(f"Максимальная прибыль: {max_profit}\n")
    else:
        print("\nНедостаточно данных для анализа")
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write("Недостаточно данных для анализа\n")
