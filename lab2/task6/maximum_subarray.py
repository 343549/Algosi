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
    # Установка кодировки для вывода
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    # Чтение данных из файла input.txt
    # Формат:
    # Строка 1: Название компании
    # Строка 2: Период (например, "01.01.2024 - 31.01.2024")
    # Далее: строки с датой и ценой (формат: "YYYY-MM-DD цена")
    
    print("=" * 60)
    print("Задача 6: Поиск максимальной прибыли")
    print("=" * 60)
    
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Удаляем пробелы и пустые строки
        lines = [line.strip() for line in lines if line.strip()]
        
        if len(lines) < 3:
            print("Ошибка: недостаточно данных в файле input.txt")
            exit(1)
        
        company_name = lines[0]
        period = lines[1]
        
        # Читаем данные о ценах
        stock_data = []
        for line in lines[2:]:
            parts = line.split()
            if len(parts) >= 2:
                date = parts[0]
                try:
                    price = float(parts[1])
                    stock_data.append((date, price))
                except ValueError:
                    print(f"Предупреждение: не удалось распарсить цену в строке: {line}")
        
        if len(stock_data) < 2:
            print("Ошибка: недостаточно данных о ценах (нужно минимум 2 дня)")
            exit(1)
        
        # Извлекаем цены и даты
        prices = [price for _, price in stock_data]
        dates = [date for date, _ in stock_data]
        
        print(f"Компания: {company_name}")
        print(f"Период: {period}")
        print(f"\nЦены акций по дням (показаны первые и последние 5 дней):")
        for i, (date, price) in enumerate(stock_data):
            if i < 5 or i >= len(stock_data) - 5:
                print(f"  {date}: {price:.2f}")
            elif i == 5:
                print(f"  ... (пропущено {len(stock_data) - 10} дней) ...")
        
        # Вычисляем изменения цен
        price_changes = calculate_price_changes(prices)
        print(f"\nВсего дней: {len(stock_data)}")
        print(f"Изменений цен: {len(price_changes)}")
        
        # Находим максимальный подмассив (максимальную прибыль)
        buy_day_idx, sell_day_idx, max_profit = find_maximum_subarray(price_changes, 0, len(price_changes) - 1)
        
        # Индексы для дат: buy_day_idx соответствует дню покупки, sell_day_idx+1 - дню продажи
        buy_date = dates[buy_day_idx]
        sell_date = dates[sell_day_idx + 1]
        buy_price = prices[buy_day_idx]
        sell_price = prices[sell_day_idx + 1]
        
        print(f"\n{'='*60}")
        print("РЕЗУЛЬТАТ:")
        print(f"{'='*60}")
        print(f"Дата покупки: {buy_date} (цена: {buy_price:.2f})")
        print(f"Дата продажи: {sell_date} (цена: {sell_price:.2f})")
        print(f"Максимальная прибыль: {max_profit:.2f}")
        print(f"{'='*60}")
        
        # Запись в файл
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(f"Компания: {company_name}\n")
            f.write(f"Период изменения цен акций: {period}\n")
            f.write(f"Дата покупки: {buy_date}\n")
            f.write(f"Дата продажи: {sell_date}\n")
            f.write(f"Максимальная прибыль: {max_profit:.2f}\n")
            
    except FileNotFoundError:
        print("Ошибка: файл input.txt не найден")
        exit(1)
    except Exception as e:
        print(f"Ошибка при обработке данных: {e}")
        exit(1)
