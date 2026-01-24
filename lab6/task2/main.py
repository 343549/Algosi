#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача 2: Телефонная книга
Реализация простого менеджера телефонной книги.
Используется хеш-таблица для хранения номеров телефонов и имен.
"""

class PhoneBook:
    def __init__(self, size=1000000):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, number):
        """Хеш-функция для номера телефона"""
        return number % self.size
    
    def add(self, number, name):
        """Добавить или обновить запись в телефонной книге"""
        h = self._hash(number)
        # Используем открытую адресацию с линейным пробированием
        while self.table[h] is not None and self.table[h][0] != number:
            h = (h + 1) % self.size
        
        self.table[h] = (number, name)
    
    def delete(self, number):
        """Удалить запись из телефонной книги"""
        h = self._hash(number)
        start_h = h
        while self.table[h] is not None:
            if self.table[h][0] == number:
                self.table[h] = None
                return
            h = (h + 1) % self.size
            if h == start_h:
                break
    
    def find(self, number):
        """Найти имя по номеру телефона"""
        h = self._hash(number)
        start_h = h
        while self.table[h] is not None:
            if self.table[h][0] == number:
                return self.table[h][1]
            h = (h + 1) % self.size
            if h == start_h:
                break
        return "not found"


def main():
    # Чтение входных данных
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')
    output_path = os.path.join(script_dir, 'output.txt')
    
    with open(input_path, 'r', encoding='utf-8') as f:
        n = int(f.readline().strip())
        operations = []
        for _ in range(n):
            line = f.readline().strip().split(maxsplit=2)
            op = line[0]
            if op == 'add':
                number = int(line[1])
                name = line[2]
                operations.append((op, number, name))
            elif op == 'del':
                number = int(line[1])
                operations.append((op, number, None))
            elif op == 'find':
                number = int(line[1])
                operations.append((op, number, None))
    
    # Создание телефонной книги
    phone_book = PhoneBook()
    results = []
    
    # Обработка операций
    for op, number, name in operations:
        if op == 'add':
            phone_book.add(number, name)
        elif op == 'del':
            phone_book.delete(number)
        elif op == 'find':
            result = phone_book.find(number)
            results.append(result)
    
    # Запись результатов
    with open(output_path, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(result + '\n')
    
    print("Task 2 completed successfully!")
    print(f"Processed operations: {n}")
    print(f"Performed searches: {len(results)}")


if __name__ == '__main__':
    main()
