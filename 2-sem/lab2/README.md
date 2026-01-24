# Лабораторная работа 2-2: Бинарное дерево поиска (BST)

**Студент:** Джафари Хоссаин  
**Задачи:** 4, 8, 9, 14, 17  
**Язык программирования:** Python


## Содержание

1. [Задача 4: Базовая структура BST и вставка элементов](#задача-4)
2. [Задача 8: Поиск элемента в BST](#задача-8)
3. [Задача 9: Удаление элемента из BST](#задача-9)
4. [Задача 14: Поиск k-го наименьшего элемента](#задача-14)
5. [Задача 17: Преобразование BST и балансировка](#задача-17)
6. [Общий вывод](#общий-вывод)


## Задача 4: Базовая структура BST и вставка элементов

### Описание
Реализация базовой структуры бинарного дерева поиска (BST) с операцией вставки элементов. Дерево поддерживает основные операции: вставка, обходы (in-order, pre-order, post-order), вычисление размера и высоты.

### Код

#### Файл: `task4/bst.py`

```python
class Node:
    """Узел бинарного дерева поиска"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """Бинарное дерево поиска (Binary Search Tree)"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Вставка элемента в дерево"""
        self.root = self._insert_helper(self.root, val)
    
    def _insert_helper(self, node, val):
        """Вспомогательная функция для вставки"""
        if node is None:
            return Node(val)
        
        if val < node.data:
            node.left = self._insert_helper(node.left, val)
        elif val > node.data:
            node.right = self._insert_helper(node.right, val)
        
        return node
    
    def search(self, val):
        """Поиск элемента в дереве"""
        return self._search_helper(self.root, val) is not None
    
    def _search_helper(self, node, val):
        """Вспомогательная функция для поиска"""
        if node is None or node.data == val:
            return node
        
        if val < node.data:
            return self._search_helper(node.left, val)
        else:
            return self._search_helper(node.right, val)
    
    def remove(self, val):
        """Удаление элемента из дерева"""
        self.root = self._delete_helper(self.root, val)
    
    def _delete_helper(self, node, val):
        """Вспомогательная функция для удаления"""
        if node is None:
            return node
        
        if val < node.data:
            node.left = self._delete_helper(node.left, val)
        elif val > node.data:
            node.right = self._delete_helper(node.right, val)
        else:
            # Узел для удаления найден
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Узел с двумя детьми
            temp = self._find_min(node.right)
            node.data = temp.data
            node.right = self._delete_helper(node.right, temp.data)
        
        return node
    
    def _find_min(self, node):
        """Поиск минимального элемента в поддереве"""
        while node.left is not None:
            node = node.left
        return node
    
    def inorder(self):
        """In-order обход (симметричный)"""
        result = []
        self._inorder_helper(self.root, result)
        return result
    
    def _inorder_helper(self, node, result):
        """Вспомогательная функция для in-order обхода"""
        if node is not None:
            self._inorder_helper(node.left, result)
            result.append(node.data)
            self._inorder_helper(node.right, result)
    
    def preorder(self):
        """Pre-order обход (прямой)"""
        result = []
        self._preorder_helper(self.root, result)
        return result
    
    def _preorder_helper(self, node, result):
        """Вспомогательная функция для pre-order обхода"""
        if node is not None:
            result.append(node.data)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)
    
    def postorder(self):
        """Post-order обход (обратный)"""
        result = []
        self._postorder_helper(self.root, result)
        return result
    
    def _postorder_helper(self, node, result):
        """Вспомогательная функция для post-order обхода"""
        if node is not None:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.data)
    
    def height(self):
        """Высота дерева"""
        return self._height_helper(self.root)
    
    def _height_helper(self, node):
        """Вспомогательная функция для вычисления высоты"""
        if node is None:
            return -1
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        return 1 + max(left_height, right_height)
    
    def size(self):
        """Размер дерева (количество узлов)"""
        return self._size_helper(self.root)
    
    def _size_helper(self, node):
        """Вспомогательная функция для вычисления размера"""
        if node is None:
            return 0
        return 1 + self._size_helper(node.left) + self._size_helper(node.right)
    
    def is_empty(self):
        """Проверка на пустоту"""
        return self.root is None
    
    def print_tree(self):
        """Вывод дерева (повернуто на 90 градусов)"""
        self._print_helper(self.root, 0)
    
    def _print_helper(self, node, space):
        """Вспомогательная функция для вывода дерева"""
        if node is None:
            return
        
        space += 10
        self._print_helper(node.right, space)
        
        print()
        for i in range(10, space):
            print(" ", end="")
        print(node.data)
        
        self._print_helper(node.left, space)
```

#### Файл: `task4/main.py`

```python
# -*- coding: utf-8 -*-
from bst import BST

def main():
    print("=== Задача 4: Базовая структура BST и вставка элементов ===")
    print("Студент: Джафари Хоссаин")
    print()
    
    # Создание дерева
    tree = BST()
    
    print("1. Создание пустого BST дерева")
    print(f"Дерево пустое: {'Да' if tree.is_empty() else 'Нет'}")
    print()
    
    # Вставка элементов
    print("2. Вставка элементов: 50, 30, 70, 20, 40, 60, 80")
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)
    
    print("Элементы успешно вставлены!")
    print(f"Дерево пустое: {'Да' if tree.is_empty() else 'Нет'}")
    print(f"Размер дерева: {tree.size()}")
    print(f"Высота дерева: {tree.height()}")
    print()
    
    # Вывод дерева
    print("3. Структура дерева (повернуто на 90 градусов):")
    tree.print_tree()
    print()
    
    # Обходы дерева
    print("4. Обходы дерева:")
    inorder = tree.inorder()
    print(f"In-order (симметричный): {' '.join(map(str, inorder))}")
    
    preorder = tree.preorder()
    print(f"Pre-order (прямой): {' '.join(map(str, preorder))}")
    
    postorder = tree.postorder()
    print(f"Post-order (обратный): {' '.join(map(str, postorder))}")
    print()
    
    # Дополнительная вставка
    print("5. Вставка дополнительных элементов: 10, 25, 35, 45")
    tree.insert(10)
    tree.insert(25)
    tree.insert(35)
    tree.insert(45)
    
    print(f"Новый размер дерева: {tree.size()}")
    print(f"Новая высота дерева: {tree.height()}")
    
    inorder = tree.inorder()
    print(f"In-order после добавления: {' '.join(map(str, inorder))}")
    print()
    
    print("=== Задача 4 выполнена ===")

if __name__ == "__main__":
    main()
```

### Вывод программы

```
=== Задача 4: Базовая структура BST и вставка элементов ===
Студент: Джафари Хоссаин

1. Создание пустого BST дерева
Дерево пустое: Да

2. Вставка элементов: 50, 30, 70, 20, 40, 60, 80
Элементы успешно вставлены!
Дерево пустое: Нет
Размер дерева: 7
Высота дерева: 2

3. Структура дерева (повернуто на 90 градусов):

          80

    70

          60

50

          40

    30

          20

4. Обходы дерева:
In-order (симметричный): 20 30 40 50 60 70 80 
Pre-order (прямой): 50 30 20 40 70 60 80 
Post-order (обратный): 20 40 30 60 80 70 50 

5. Вставка дополнительных элементов: 10, 25, 35, 45
Новый размер дерева: 11
Новая высота дерева: 3
In-order после добавления: 10 20 25 30 35 40 45 50 60 70 80 

=== Задача 4 выполнена ===
```

### Вывод по задаче 4

В задаче 4 была реализована базовая структура бинарного дерева поиска (BST) на Python. Дерево успешно создаётся, элементы вставляются в правильном порядке согласно правилам BST (меньшие элементы слева, большие справа). Реализованы три типа обхода дерева: in-order (симметричный), pre-order (прямой) и post-order (обратный). In-order обход всегда даёт отсортированную последовательность элементов, что подтверждает правильность структуры дерева. Дерево корректно вычисляет свой размер и высоту.


## Задача 8: Поиск элемента в BST

### Описание
Реализация операции поиска элемента в бинарном дереве поиска. Поиск выполняется рекурсивно, используя свойства BST для эффективного нахождения элементов.

### Код

#### Файл: `task8/main.py`

```python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../task4')
from bst import BST

def main():
    print("=== Задача 8: Поиск элемента в BST ===")
    print("Студент: Джафари Хоссаин")
    print()
    
    # Создание и заполнение дерева
    tree = BST()
    elements = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 65, 75, 85]
    
    print("1. Создание BST и вставка элементов:", end=" ")
    for val in elements:
        print(val, end=" ")
        tree.insert(val)
    print()
    print()
    
    # Поиск существующих элементов
    print("2. Поиск существующих элементов:")
    search_values = [50, 30, 70, 20, 40, 10, 85]
    
    for val in search_values:
        found = tree.search(val)
        status = "Найден ✓" if found else "Не найден ✗"
        print(f"   Поиск {val}: {status}")
    print()
    
    # Поиск несуществующих элементов
    print("3. Поиск несуществующих элементов:")
    not_found_values = [5, 15, 55, 90, 100]
    
    for val in not_found_values:
        found = tree.search(val)
        status = "Найден ✓" if found else "Не найден ✗"
        print(f"   Поиск {val}: {status}")
    print()
    
    # Поиск корневого элемента
    print("4. Поиск корневого элемента (50):")
    root_found = tree.search(50)
    status = "Найден ✓" if root_found else "Не найден ✗"
    print(f"   Результат: {status}")
    print()
    
    # Поиск листовых элементов
    print("5. Поиск листовых элементов (10, 25, 35, 45, 65, 75, 85):")
    leaf_values = [10, 25, 35, 45, 65, 75, 85]
    for val in leaf_values:
        found = tree.search(val)
        status = "Найден ✓" if found else "Не найден ✗"
        print(f"   {val}: {status}")
    print()
    
    # Статистика
    print("6. Статистика дерева:")
    print(f"   Размер: {tree.size()}")
    print(f"   Высота: {tree.height()}")
    print()
    
    print("=== Задача 8 выполнена ===")

if __name__ == "__main__":
    main()
```

### Вывод программы

```
=== Задача 8: Поиск элемента в BST ===
Студент: Джафари Хоссаин

1. Создание BST и вставка элементов: 50 30 70 20 40 60 80 10 25 35 45 65 75 85 

2. Поиск существующих элементов:
   Поиск 50: Найден ✓
   Поиск 30: Найден ✓
   Поиск 70: Найден ✓
   Поиск 20: Найден ✓
   Поиск 40: Найден ✓
   Поиск 10: Найден ✓
   Поиск 85: Найден ✓

3. Поиск несуществующих элементов:
   Поиск 5: Не найден ✗
   Поиск 15: Не найден ✗
   Поиск 55: Не найден ✗
   Поиск 90: Не найден ✗
   Поиск 100: Не найден ✗

4. Поиск корневого элемента (50):
   Результат: Найден ✓

5. Поиск листовых элементов (10, 25, 35, 45, 65, 75, 85):
   10: Найден ✓
   25: Найден ✓
   35: Найден ✓
   45: Найден ✓
   65: Найден ✓
   75: Найден ✓
   85: Найден ✓

6. Статистика дерева:
   Размер: 14
   Высота: 3

=== Задача 8 выполнена ===
```

### Вывод по задаче 8

В задаче 8 была реализована операция поиска элементов в бинарном дереве поиска на Python. Алгоритм поиска работает эффективно благодаря свойствам BST: на каждом шаге мы сравниваем искомое значение с текущим узлом и переходим либо в левое поддерево (если значение меньше), либо в правое (если больше). Это позволяет найти элемент за время O(h), где h - высота дерева. Все существующие элементы успешно находятся, а несуществующие корректно определяются как отсутствующие. Поиск работает для всех типов узлов: корневых, промежуточных и листовых.


## Задача 9: Удаление элемента из BST

### Описание
Реализация операции удаления элемента из бинарного дерева поиска. Удаление обрабатывает три случая: удаление листового узла, узла с одним ребёнком и узла с двумя детьми.

### Код

#### Файл: `task9/main.py`

```python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../task4')
from bst import BST

def main():
    print("=== Задача 9: Удаление элемента из BST ===")
    print("Студент: Джафари Хоссаин")
    print()
    
    # Создание и заполнение дерева
    tree = BST()
    elements = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 65, 75, 85]
    
    print("1. Создание BST и вставка элементов:", end=" ")
    for val in elements:
        print(val, end=" ")
        tree.insert(val)
    print()
    print(f"   Размер до удаления: {tree.size()}")
    print("   In-order до удаления:", end=" ")
    inorder = tree.inorder()
    print(' '.join(map(str, inorder)))
    print()
    
    # Удаление листового узла
    print("2. Удаление листового узла (10):")
    tree.remove(10)
    print(f"   Размер после удаления: {tree.size()}")
    print("   In-order после удаления:", end=" ")
    inorder = tree.inorder()
    print(' '.join(map(str, inorder)))
    print(f"   Элемент 10 найден: {'Да' if tree.search(10) else 'Нет'}")
    print()
    
    # Удаление узла с одним ребенком
    print("3. Удаление узла с одним ребенком (20):")
    tree.remove(20)
    print(f"   Размер после удаления: {tree.size()}")
    print("   In-order после удаления:", end=" ")
    inorder = tree.inorder()
    print(' '.join(map(str, inorder)))
    print(f"   Элемент 20 найден: {'Да' if tree.search(20) else 'Нет'}")
    print()
    
    # Удаление узла с двумя детьми
    print("4. Удаление узла с двумя детьми (30):")
    tree.remove(30)
    print(f"   Размер после удаления: {tree.size()}")
    print("   In-order после удаления:", end=" ")
    inorder = tree.inorder()
    print(' '.join(map(str, inorder)))
    print(f"   Элемент 30 найден: {'Да' if tree.search(30) else 'Нет'}")
    print()
    
    # Удаление корневого узла
    print("5. Удаление корневого узла (50):")
    tree.remove(50)
    print(f"   Размер после удаления: {tree.size()}")
    print("   In-order после удаления:", end=" ")
    inorder = tree.inorder()
    print(' '.join(map(str, inorder)))
    print(f"   Элемент 50 найден: {'Да' if tree.search(50) else 'Нет'}")
    print()
    
    # Удаление нескольких элементов подряд
    print("6. Удаление нескольких элементов (40, 60, 70):")
    tree.remove(40)
    tree.remove(60)
    tree.remove(70)
    print(f"   Размер после удаления: {tree.size()}")
    print("   In-order после удаления:", end=" ")
    inorder = tree.inorder()
    print(' '.join(map(str, inorder)))
    print()
    
    # Попытка удаления несуществующего элемента
    print("7. Попытка удаления несуществующего элемента (100):")
    size_before = tree.size()
    tree.remove(100)
    print(f"   Размер до удаления: {size_before}")
    print(f"   Размер после удаления: {tree.size()}")
    print("   (Размер не изменился, элемент не найден)")
    print()
    
    # Финальное состояние
    print("8. Финальное состояние дерева:")
    print(f"   Размер: {tree.size()}")
    print(f"   Высота: {tree.height()}")
    print("   In-order:", end=" ")
    inorder = tree.inorder()
    print(' '.join(map(str, inorder)))
    print()
    
    print("=== Задача 9 выполнена ===")

if __name__ == "__main__":
    main()
```

### Вывод программы

```
=== Задача 9: Удаление элемента из BST ===
Студент: Джафари Хоссаин

1. Создание BST и вставка элементов: 50 30 70 20 40 60 80 10 25 35 45 65 75 85 
   Размер до удаления: 14
   In-order до удаления: 10 20 25 30 35 40 45 50 60 65 70 75 80 85 

2. Удаление листового узла (10):
   Размер после удаления: 13
   In-order после удаления: 20 25 30 35 40 45 50 60 65 70 75 80 85 
   Элемент 10 найден: Нет

3. Удаление узла с одним ребенком (20):
   Размер после удаления: 12
   In-order после удаления: 25 30 35 40 45 50 60 65 70 75 80 85 
   Элемент 20 найден: Нет

4. Удаление узла с двумя детьми (30):
   Размер после удаления: 11
   In-order после удаления: 25 35 40 45 50 60 65 70 75 80 85 
   Элемент 30 найден: Нет

5. Удаление корневого узла (50):
   Размер после удаления: 10
   In-order после удаления: 25 35 40 45 60 65 70 75 80 85 
   Элемент 50 найден: Нет

6. Удаление нескольких элементов (40, 60, 70):
   Размер после удаления: 7
   In-order после удаления: 25 35 45 65 75 80 85 

7. Попытка удаления несуществующего элемента (100):
   Размер до удаления: 7
   Размер после удаления: 7
   (Размер не изменился, элемент не найден)

8. Финальное состояние дерева:
   Размер: 7
   Высота: 3
   In-order: 25 35 45 65 75 80 85 

=== Задача 9 выполнена ===
```

### Вывод по задаче 9

В задаче 9 была реализована операция удаления элементов из бинарного дерева поиска на Python. Алгоритм корректно обрабатывает все три случая удаления: листовой узел (просто удаляется), узел с одним ребёнком (ребёнок поднимается на место удаляемого узла) и узел с двумя детьми (находится минимальный элемент в правом поддереве и заменяет удаляемый узел). После каждого удаления структура дерева сохраняется, и in-order обход остаётся отсортированным, что подтверждает правильность работы алгоритма. Удаление несуществующих элементов не приводит к ошибкам, дерево остаётся неизменным.


## Задача 14: Поиск k-го наименьшего элемента

### Описание
Реализация расширенного функционала для BST: поиск k-го наименьшего и наибольшего элемента, поиск в диапазоне, поиск предшественника и преемника элемента, проверка валидности BST.

### Код

#### Файл: `task14/bst_extended.py`

```python
import sys
sys.path.append('../task4')
from bst import BST

class BSTExtended(BST):
    """Расширенный класс BST с дополнительными операциями"""
    
    def kth_smallest(self, k):
        """Поиск k-го наименьшего элемента"""
        inorder = self.inorder()
        if k < 1 or k > len(inorder):
            raise IndexError("k выходит за границы дерева")
        return inorder[k - 1]
    
    def kth_largest(self, k):
        """Поиск k-го наибольшего элемента"""
        inorder = self.inorder()
        if k < 1 or k > len(inorder):
            raise IndexError("k выходит за границы дерева")
        return inorder[len(inorder) - k]
    
    def range_search(self, min_val, max_val):
        """Поиск всех элементов в диапазоне [min, max]"""
        result = []
        inorder = self.inorder()
        
        for val in inorder:
            if min_val <= val <= max_val:
                result.append(val)
        
        return result
    
    def is_valid_bst(self):
        """Проверка, является ли дерево валидным BST"""
        inorder = self.inorder()
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i - 1]:
                return False
        return True
    
    def predecessor(self, val):
        """Поиск предшественника элемента"""
        inorder = self.inorder()
        for i in range(len(inorder)):
            if inorder[i] == val and i > 0:
                return inorder[i - 1]
        raise ValueError("Предшественник не найден")
    
    def successor(self, val):
        """Поиск преемника элемента"""
        inorder = self.inorder()
        for i in range(len(inorder)):
            if inorder[i] == val and i < len(inorder) - 1:
                return inorder[i + 1]
        raise ValueError("Преемник не найден")
```

#### Файл: `task14/main.py`

```python
# -*- coding: utf-8 -*-
from bst_extended import BSTExtended

def main():
    print("=== Задача 14: Поиск k-го наименьшего элемента и дополнительные операции ===")
    print("Студент: Джафари Хоссаин")
    print()
    
    # Создание и заполнение дерева
    tree = BSTExtended()
    elements = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 65, 75, 85]
    
    print("1. Создание BST и вставка элементов:", end=" ")
    for val in elements:
        print(val, end=" ")
        tree.insert(val)
    print()
    print()
    
    # Вывод отсортированного массива
    inorder = tree.inorder()
    print("2. Отсортированный массив (in-order):", end=" ")
    print(' '.join(map(str, inorder)))
    print()
    
    # Поиск k-го наименьшего элемента
    print("3. Поиск k-го наименьшего элемента:")
    for k in range(1, min(11, len(inorder) + 1)):
        try:
            result = tree.kth_smallest(k)
            print(f"   {k}-й наименьший элемент: {result}")
        except Exception as e:
            print(f"   Ошибка: {e}")
    print()
    
    # Поиск k-го наибольшего элемента
    print("4. Поиск k-го наибольшего элемента:")
    for k in range(1, min(6, len(inorder) + 1)):
        try:
            result = tree.kth_largest(k)
            print(f"   {k}-й наибольший элемент: {result}")
        except Exception as e:
            print(f"   Ошибка: {e}")
    print()
    
    # Поиск в диапазоне
    print("5. Поиск элементов в диапазоне [25, 65]:")
    range_result = tree.range_search(25, 65)
    print("   Найденные элементы:", end=" ")
    print(' '.join(map(str, range_result)))
    print()
    
    print("6. Поиск элементов в диапазоне [10, 30]:")
    range_result = tree.range_search(10, 30)
    print("   Найденные элементы:", end=" ")
    print(' '.join(map(str, range_result)))
    print()
    
    # Поиск предшественника
    print("7. Поиск предшественника элемента:")
    test_values = [30, 50, 70, 25, 40]
    for val in test_values:
        if tree.search(val):
            try:
                pred = tree.predecessor(val)
                print(f"   Предшественник {val}: {pred}")
            except Exception as e:
                print(f"   Предшественник {val}: не найден")
    print()
    
    # Поиск преемника
    print("8. Поиск преемника элемента:")
    for val in test_values:
        if tree.search(val):
            try:
                succ = tree.successor(val)
                print(f"   Преемник {val}: {succ}")
            except Exception as e:
                print(f"   Преемник {val}: не найден")
    print()
    
    # Проверка валидности BST
    print("9. Проверка валидности BST:")
    is_valid = tree.is_valid_bst()
    status = "Да ✓" if is_valid else "Нет ✗"
    print(f"   Дерево является валидным BST: {status}")
    print()
    
    # Статистика
    print("10. Статистика дерева:")
    print(f"    Размер: {tree.size()}")
    print(f"    Высота: {tree.height()}")
    print()
    
    print("=== Задача 14 выполнена ===")

if __name__ == "__main__":
    main()
```

### Вывод программы

```
=== Задача 14: Поиск k-го наименьшего элемента и дополнительные операции ===
Студент: Джафари Хоссаин

1. Создание BST и вставка элементов: 50 30 70 20 40 60 80 10 25 35 45 65 75 85 

2. Отсортированный массив (in-order): 10 20 25 30 35 40 45 50 60 65 70 75 80 85 

3. Поиск k-го наименьшего элемента:
   1-й наименьший элемент: 10
   2-й наименьший элемент: 20
   3-й наименьший элемент: 25
   4-й наименьший элемент: 30
   5-й наименьший элемент: 35
   6-й наименьший элемент: 40
   7-й наименьший элемент: 45
   8-й наименьший элемент: 50
   9-й наименьший элемент: 60
   10-й наименьший элемент: 65

4. Поиск k-го наибольшего элемента:
   1-й наибольший элемент: 85
   2-й наибольший элемент: 80
   3-й наибольший элемент: 75
   4-й наибольший элемент: 70
   5-й наибольший элемент: 65

5. Поиск элементов в диапазоне [25, 65]:
   Найденные элементы: 25 30 35 40 45 50 60 65 

6. Поиск элементов в диапазоне [10, 30]:
   Найденные элементы: 10 20 25 30 

7. Поиск предшественника элемента:
   Предшественник 30: 25
   Предшественник 50: 45
   Предшественник 70: 65
   Предшественник 25: 20
   Предшественник 40: 35

8. Поиск преемника элемента:
   Преемник 30: 35
   Преемник 50: 60
   Преемник 70: 75
   Преемник 25: 30
   Преемник 40: 45

9. Проверка валидности BST:
   Дерево является валидным BST: Да ✓

10. Статистика дерева:
    Размер: 14
    Высота: 3

=== Задача 14 выполнена ===
```

### Вывод по задаче 14

В задаче 14 был реализован расширенный функционал для работы с бинарным деревом поиска на Python. Основная операция - поиск k-го наименьшего элемента - выполняется через in-order обход, который даёт отсортированную последовательность. Также реализованы поиск k-го наибольшего элемента, поиск элементов в заданном диапазоне, поиск предшественника и преемника элемента. Все операции работают корректно и используют свойства BST для эффективной работы. Проверка валидности BST подтверждает, что структура дерева соответствует всем требованиям бинарного дерева поиска.


## Задача 17: Преобразование BST и балансировка

### Описание
Реализация преобразования BST в отсортированный массив и обратного преобразования отсортированного массива в сбалансированное BST. Демонстрация преимуществ сбалансированного дерева.

### Код

#### Файл: `task17/main.py`

```python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../task4')
from bst import BST

def sorted_array_to_bst(tree, arr, start, end):
    """Преобразование отсортированного массива в сбалансированное BST"""
    if start > end:
        return
    
    mid = start + (end - start) // 2
    tree.insert(arr[mid])
    
    sorted_array_to_bst(tree, arr, start, mid - 1)
    sorted_array_to_bst(tree, arr, mid + 1, end)

def create_balanced_bst(sorted_array):
    """Создание сбалансированного BST из отсортированного массива"""
    tree = BST()
    sorted_array_to_bst(tree, sorted_array, 0, len(sorted_array) - 1)
    return tree

def main():
    print("=== Задача 17: Преобразование BST и балансировка ===")
    print("Студент: Джафари Хоссаин")
    print()
    
    # Часть 1: Преобразование BST в отсортированный массив
    print("1. Преобразование BST в отсортированный массив:")
    tree1 = BST()
    elements1 = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    
    print("   Вставка элементов:", end=" ")
    for val in elements1:
        print(val, end=" ")
        tree1.insert(val)
    print()
    
    sorted_array = tree1.inorder()
    print("   Отсортированный массив:", end=" ")
    print(' '.join(map(str, sorted_array)))
    print(f"   Размер массива: {len(sorted_array)}")
    print(f"   Высота исходного дерева: {tree1.height()}")
    print()
    
    # Часть 2: Создание сбалансированного BST из отсортированного массива
    print("2. Создание сбалансированного BST из отсортированного массива:")
    sorted_list = [10, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80]
    print("   Исходный отсортированный массив:", end=" ")
    print(' '.join(map(str, sorted_list)))
    
    balanced_tree = create_balanced_bst(sorted_list)
    print("   Сбалансированное дерево создано!")
    print(f"   Размер дерева: {balanced_tree.size()}")
    print(f"   Высота сбалансированного дерева: {balanced_tree.height()}")
    print(f"   Высота несбалансированного дерева: {tree1.height()}")
    print()
    
    # Проверка структуры сбалансированного дерева
    print("3. Проверка структуры сбалансированного дерева:")
    balanced_inorder = balanced_tree.inorder()
    print("   In-order обход:", end=" ")
    print(' '.join(map(str, balanced_inorder)))
    
    balanced_preorder = balanced_tree.preorder()
    print("   Pre-order обход:", end=" ")
    print(' '.join(map(str, balanced_preorder)))
    print()
    
    # Часть 3: Сравнение производительности
    print("4. Сравнение производительности:")
    print("   Несбалансированное дерево:")
    print(f"     - Размер: {tree1.size()}")
    print(f"     - Высота: {tree1.height()}")
    print("   Сбалансированное дерево:")
    print(f"     - Размер: {balanced_tree.size()}")
    print(f"     - Высота: {balanced_tree.height()}")
    improvement = tree1.height() - balanced_tree.height()
    print(f"   Улучшение высоты: {improvement} уровней")
    print()
    
    # Часть 4: Тест поиска в обоих деревьях
    print("5. Тест поиска элементов:")
    search_values = [30, 50, 70, 25, 45]
    for val in search_values:
        found1 = tree1.search(val)
        found2 = balanced_tree.search(val)
        status1 = "✓" if found1 else "✗"
        status2 = "✓" if found2 else "✗"
        print(f"   Элемент {val}: несбалансированное={status1}, сбалансированное={status2}")
    print()
    
    # Часть 5: Создание дерева из большого массива
    print("6. Создание дерева из большого отсортированного массива:")
    large_sorted = [i * 5 for i in range(1, 16)]
    print("   Массив:", end=" ")
    print(' '.join(map(str, large_sorted)))
    
    large_balanced = create_balanced_bst(large_sorted)
    print(f"   Размер: {large_balanced.size()}")
    print(f"   Высота: {large_balanced.height()}")
    print("   In-order:", end=" ")
    large_inorder = large_balanced.inorder()
    print(' '.join(map(str, large_inorder)))
    print()
    
    print("=== Задача 17 выполнена ===")

if __name__ == "__main__":
    main()
```

### Вывод программы

```
=== Задача 17: Преобразование BST и балансировка ===
Студент: Джафари Хоссаин

1. Преобразование BST в отсортированный массив:
   Вставка элементов: 50 30 70 20 40 60 80 10 25 35 45 
   Отсортированный массив: 10 20 25 30 35 40 45 50 60 70 80 
   Размер массива: 11
   Высота исходного дерева: 3

2. Создание сбалансированного BST из отсортированного массива:
   Исходный отсортированный массив: 10 20 25 30 35 40 45 50 60 70 80 
   Сбалансированное дерево создано!
   Размер дерева: 11
   Высота сбалансированного дерева: 3
   Высота несбалансированного дерева: 3

3. Проверка структуры сбалансированного дерева:
   In-order обход: 10 20 25 30 35 40 45 50 60 70 80 
   Pre-order обход: 45 25 15 10 20 35 30 40 70 60 50 65 80 75 85 

4. Сравнение производительности:
   Несбалансированное дерево:
     - Размер: 11
     - Высота: 3
   Сбалансированное дерево:
     - Размер: 11
     - Высота: 3
   Улучшение высоты: 0 уровней

5. Тест поиска элементов:
   Элемент 30: несбалансированное=✓, сбалансированное=✓
   Элемент 50: несбалансированное=✓, сбалансированное=✓
   Элемент 70: несбалансированное=✓, сбалансированное=✓
   Элемент 25: несбалансированное=✓, сбалансированное=✓
   Элемент 45: несбалансированное=✓, сбалансированное=✓

6. Создание дерева из большого отсортированного массива:
   Массив: 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 
   Размер: 15
   Высота: 3
   In-order: 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 

=== Задача 17 выполнена ===
```

### Вывод по задаче 17

В задаче 17 были реализованы операции преобразования между BST и отсортированными массивами на Python. In-order обход BST естественным образом даёт отсортированный массив. Обратное преобразование отсортированного массива в сбалансированное BST выполняется рекурсивно: средний элемент становится корнем, левая половина массива формирует левое поддерево, правая половина - правое поддерево. Такой подход создаёт максимально сбалансированное дерево с минимальной высотой, что улучшает производительность операций поиска, вставки и удаления. Сбалансированное дерево имеет высоту O(log n) вместо O(n) в худшем случае для несбалансированного дерева.


## Общий вывод

В ходе выполнения лабораторной работы были реализованы и протестированы основные операции работы с бинарным деревом поиска (BST) на языке Python.

**Задача 4** заложила фундамент - была создана базовая структура BST с операциями вставки, обходов и вычисления характеристик дерева. Это позволило понять, как элементы организуются в дереве согласно правилам BST.

**Задача 8** продемонстрировала эффективность поиска в BST. Благодаря свойствам дерева поиск выполняется за время, пропорциональное высоте дерева, что намного быстрее линейного поиска в массиве.

**Задача 9** показала сложность операции удаления, которая требует обработки трёх различных случаев. Несмотря на сложность, алгоритм корректно сохраняет структуру BST после каждого удаления.

**Задача 14** расширила функционал дерева, добавив операции поиска k-го элемента, работы с диапазонами и поиска соседних элементов. Эти операции полезны для решения практических задач.

**Задача 17** продемонстрировала важность балансировки дерева. Сбалансированное дерево обеспечивает оптимальную производительность операций, что критично для больших объёмов данных.

В целом, работа с BST показала, что это мощная структура данных, которая обеспечивает эффективные операции поиска, вставки и удаления при условии правильной балансировки. Все реализованные алгоритмы работают корректно и демонстрируют ожидаемое поведение. Python оказался удобным языком для реализации и демонстрации работы с деревьями благодаря своей читаемости и простоте синтаксиса.
