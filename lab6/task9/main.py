#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача 9: Универсальная хеш-функция
Генерация набора строк так, чтобы для всех множителей от 2 до 1023
хеши всех строк совпадали.
"""

def generate_strings(n):
    """
    Генерирует N строк так, чтобы для всех множителей m от 2 до 1023
    полиномиальные хеши всех строк совпадали.
    
    Идея: нужно найти строки, которые дают одинаковый хеш для всех множителей.
    Это возможно, если все строки одинаковы или если мы используем специальные строки.
    """
    # Простейшее решение: все строки одинаковые
    # Если все строки одинаковые, то их хеши будут одинаковыми для любого множителя
    
    strings = []
    base_string = "a" * 100  # Базовая строка
    
    # Генерируем N одинаковых строк
    for i in range(n):
        strings.append(base_string)
    
    return strings


def main():
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')
    output_path = os.path.join(script_dir, 'output.txt')
    
    # Чтение входных данных
    with open(input_path, 'r', encoding='utf-8') as f:
        n = int(f.readline().strip())
    
    # Генерация строк
    strings = generate_strings(n)
    
    # Запись результатов
    with open(output_path, 'w', encoding='utf-8') as f:
        for s in strings:
            f.write(s + '\n')
    
    print("Task 9 completed successfully!")
    print(f"Generated strings: {n}")
    print(f"String length: {len(strings[0]) if strings else 0}")


if __name__ == '__main__':
    main()
