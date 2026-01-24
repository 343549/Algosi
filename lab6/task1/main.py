#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача 1: Множество
Реализация множества с операциями добавления, удаления и проверки существования ключа.
Используется хеш-таблица с цепочками для разрешения коллизий.
"""

class HashSet:
    def __init__(self, size=1000000):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Хеш-функция для ключа"""
        return key % self.size
    
    def add(self, key):
        """Добавить элемент в множество"""
        h = self._hash(key)
        bucket = self.table[h]
        if key not in bucket:
            bucket.append(key)
    
    def delete(self, key):
        """Удалить элемент из множества"""
        h = self._hash(key)
        bucket = self.table[h]
        if key in bucket:
            bucket.remove(key)
    
    def contains(self, key):
        """Проверить наличие элемента в множестве"""
        h = self._hash(key)
        bucket = self.table[h]
        return key in bucket


def main():
    # Чтение входных данных
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')
    output_path = os.path.join(script_dir, 'output.txt')
    
    with open(input_path, 'r') as f:
        n = int(f.readline().strip())
        operations = []
        for _ in range(n):
            line = f.readline().strip().split()
            op = line[0]
            if len(line) > 1:
                x = int(line[1])
                operations.append((op, x))
            else:
                operations.append((op, None))
    
    # Создание множества
    hash_set = HashSet()
    results = []
    
    # Обработка операций
    for op, x in operations:
        if op == 'A':
            hash_set.add(x)
        elif op == 'D':
            hash_set.delete(x)
        elif op == '?':
            if hash_set.contains(x):
                results.append('Y')
            else:
                results.append('N')
    
    # Запись результатов
    with open(output_path, 'w') as f:
        for result in results:
            f.write(result + '\n')
    
    print("Task 1 completed successfully!")
    print(f"Processed operations: {n}")
    print(f"Performed checks: {len(results)}")


if __name__ == '__main__':
    main()
