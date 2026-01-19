"""Testing task 1"""
import random
import time
from task1_quicksort import randomized_quicksort, randomized_quicksort3, merge_sort

# Test 1: Example from assignment
print("Test 1: Example from assignment")
arr = [2, 3, 9, 2, 2]
arr1 = arr.copy()
arr2 = arr.copy()
arr3 = arr.copy()

randomized_quicksort(arr1, 0, len(arr1) - 1)
randomized_quicksort3(arr2, 0, len(arr2) - 1)
arr3 = merge_sort(arr3)

print(f"Original: {arr}")
print(f"QuickSort: {arr1}")
print(f"QuickSort3: {arr2}")
print(f"MergeSort: {arr3}")
print()

# Test 2: Random array
print("Test 2: Random array (1000 elements)")
arr = [random.randint(1, 1000) for _ in range(1000)]
arr1 = arr.copy()
arr2 = arr.copy()
arr3 = arr.copy()

start = time.time()
randomized_quicksort(arr1, 0, len(arr1) - 1)
t1 = time.time() - start

start = time.time()
randomized_quicksort3(arr2, 0, len(arr2) - 1)
t2 = time.time() - start

start = time.time()
arr3 = merge_sort(arr3)
t3 = time.time() - start

print(f"QuickSort: {t1:.6f} sec")
print(f"QuickSort3: {t2:.6f} sec")
print(f"MergeSort: {t3:.6f} sec")
print(f"Results match: {arr1 == arr2 == arr3}")
print()

# Test 3: Many duplicate elements
print("Test 3: Many duplicate elements (1000 elements, 5 unique)")
arr = [random.choice([1, 2, 3, 4, 5]) for _ in range(1000)]
arr1 = arr.copy()
arr2 = arr.copy()
arr3 = arr.copy()

start = time.time()
randomized_quicksort(arr1, 0, len(arr1) - 1)
t1 = time.time() - start

start = time.time()
randomized_quicksort3(arr2, 0, len(arr2) - 1)
t2 = time.time() - start

start = time.time()
arr3 = merge_sort(arr3)
t3 = time.time() - start

print(f"QuickSort: {t1:.6f} sec")
print(f"QuickSort3: {t2:.6f} sec")
print(f"MergeSort: {t3:.6f} sec")
print(f"Results match: {arr1 == arr2 == arr3}")
