#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача 4: Простой ассоциативный массив
Реализация ассоциативного массива с операциями get, prev, next, put, delete.
Используется хеш-таблица с поддержкой порядка вставки.
"""

class AssociativeArray:
    def __init__(self, size=1000000):
        self.size = size
        self.table = [None] * size
        self.order = []  # Для хранения порядка вставки
    
    def _hash(self, key):
        """Хеш-функция для ключа"""
        return hash(key) % self.size
    
    def _find_index(self, key):
        """Найти индекс ключа в таблице"""
        h = self._hash(key)
        start_h = h
        while self.table[h] is not None:
            if self.table[h] is not None and self.table[h][0] == key:
                return h
            h = (h + 1) % self.size
            if h == start_h:
                break
        return None
    
    def _find_in_order(self, key):
        """Найти позицию ключа в порядке вставки"""
        for i, (k, _) in enumerate(self.order):
            if k == key:
                return i
        return None
    
    def put(self, key, value):
        """Вставить или обновить значение"""
        h = self._find_index(key)
        
        if h is not None:
            # Ключ уже существует - обновляем значение
            self.table[h] = (key, value)
            # Обновляем в порядке
            idx = self._find_in_order(key)
            if idx is not None:
                self.order[idx] = (key, value)
        else:
            # Новый ключ - вставляем
            h = self._hash(key)
            start_h = h
            while self.table[h] is not None:
                h = (h + 1) % self.size
                if h == start_h:
                    break
            
            self.table[h] = (key, value)
            self.order.append((key, value))
    
    def get(self, key):
        """Получить значение по ключу"""
        h = self._find_index(key)
        if h is not None:
            return self.table[h][1]
        return "<none>"
    
    def prev(self, key):
        """Получить значение предыдущего ключа"""
        idx = self._find_in_order(key)
        if idx is None or idx == 0:
            return "<none>"
        return self.order[idx - 1][1]
    
    def next(self, key):
        """Получить значение следующего ключа"""
        idx = self._find_in_order(key)
        if idx is None or idx == len(self.order) - 1:
            return "<none>"
        return self.order[idx + 1][1]
    
    def delete(self, key):
        """Удалить ключ"""
        h = self._find_index(key)
        if h is not None:
            self.table[h] = None
            idx = self._find_in_order(key)
            if idx is not None:
                self.order.pop(idx)


def main():
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')
    output_path = os.path.join(script_dir, 'output.txt')
    
    # Чтение входных данных
    with open(input_path, 'r', encoding='utf-8') as f:
        n = int(f.readline().strip())
        operations = []
        for _ in range(n):
            line = f.readline().strip().split()
            op = line[0]
            if op == 'put':
                key = line[1]
                value = line[2]
                operations.append((op, key, value))
            elif op == 'get':
                key = line[1]
                operations.append((op, key, None))
            elif op == 'prev':
                key = line[1]
                operations.append((op, key, None))
            elif op == 'next':
                key = line[1]
                operations.append((op, key, None))
            elif op == 'delete':
                key = line[1]
                operations.append((op, key, None))
    
    # Создание ассоциативного массива
    arr = AssociativeArray()
    results = []
    
    # Обработка операций
    for op, key, value in operations:
        if op == 'put':
            arr.put(key, value)
        elif op == 'get':
            results.append(arr.get(key))
        elif op == 'prev':
            results.append(arr.prev(key))
        elif op == 'next':
            results.append(arr.next(key))
        elif op == 'delete':
            arr.delete(key)
    
    # Запись результатов
    with open(output_path, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(result + '\n')
    
    print("Task 4 completed successfully!")
    print(f"Processed operations: {n}")
    print(f"Performed queries: {len(results)}")


if __name__ == '__main__':
    main()
