# Selection Sort for array size of 5, 10, 20

import timeit
import random

def selectionSort (array, n):
    for i in range(n - 1):
        min_index = i
        
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        
        array[i], array[min_index] = array[min_index], array[i]
    
    return array

print("SELECTION SORT\n")

array_length_5 = [random.randint(0, 1000) for _ in range(5)]
print(f"For Array Length {len(array_length_5)}")
print(f"Original Array: {str(array_length_5)}")
start = timeit.default_timer()
print(f"Sorted Array: {str(selectionSort(array_length_5, len(array_length_5)))} within a time of {(timeit.default_timer() - start) * 1000:.2f} milliseconds\n")

array_length_10 = [random.randint(0, 1000) for _ in range(10)]
print(f"For Array Length {len(array_length_10)}")
print(f"Original Array: {str(array_length_10)}")
start = timeit.default_timer()
print(f"Sorted Array: {str(selectionSort(array_length_10, len(array_length_10)))} within a time of {(timeit.default_timer() - start) * 1000:.2f} milliseconds\n")

array_length_20 = [random.randint(0, 1000) for _ in range(20)]
print(f"For Array Length {len(array_length_20)}")
print(f"Original Array: {str(array_length_20)}")
start = timeit.default_timer()
print(f"Sorted Array: {str(selectionSort(array_length_20, len(array_length_20)))} within a time {(timeit.default_timer() - start) * 1000:.2f} milliseconds")
