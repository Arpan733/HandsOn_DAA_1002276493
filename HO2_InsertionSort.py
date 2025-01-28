# Insertion Sort for array size of 5, 10, 20

import timeit
import random

def insertionSort (array, n):
    for i in range(1, n):
        j = i - 1
        current_value = array[i]
        
        while j >= 0 and array[j] > current_value:
            array[j + 1] = array[j]
            j -= 1
    
        array[j + 1] = current_value
    
    return array

print("INSERTION SORT\n")

array_length_5 = [random.randint(0, 1000) for _ in range(5)]
print(f"For Array Length {len(array_length_5)}")
print(f"Original Array: {str(array_length_5)}")
start = timeit.default_timer()
print(f"Sorted Array: {str(insertionSort(array_length_5, len(array_length_5)))} within a time of {(timeit.default_timer() - start) * 1000:.2f} milliseconds\n")

array_length_10 = [random.randint(0, 1000) for _ in range(10)]
print(f"For Array Length {len(array_length_10)}")
print(f"Original Array: {str(array_length_10)}")
start = timeit.default_timer()
print(f"Sorted Array: {str(insertionSort(array_length_10, len(array_length_10)))} within a time of {(timeit.default_timer() - start) * 1000:.2f} milliseconds\n")

array_length_20 = [random.randint(0, 1000) for _ in range(20)]
print(f"For Array Length {len(array_length_20)}")
print(f"Original Array: {str(array_length_20)}")
start = timeit.default_timer()
print(f"Sorted Array: {str(insertionSort(array_length_20, len(array_length_20)))} within a time of {(timeit.default_timer() - start) * 1000:.2f} milliseconds")
