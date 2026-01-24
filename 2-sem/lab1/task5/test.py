"""Тестирование задачи 5"""
import subprocess
import os

# Тест 1
with open('input.txt', 'w') as f:
    f.write('6\n')
subprocess.run(['python', 'solution.py'])
print("Тест 1:")
with open('output.txt', 'r') as f:
    print(f.read())

# Тест 2
with open('input.txt', 'w') as f:
    f.write('8\n')
subprocess.run(['python', 'solution.py'])
print("\nТест 2:")
with open('output.txt', 'r') as f:
    print(f.read())

# Тест 3
with open('input.txt', 'w') as f:
    f.write('2\n')
subprocess.run(['python', 'solution.py'])
print("\nТест 3:")
with open('output.txt', 'r') as f:
    print(f.read())
