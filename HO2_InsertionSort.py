# Insertion Sort for array size of 5, 10, 20, 100, 500, 1000

import timeit
import random
import platform
import psutil

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

print("System Info:")
print(f"Operating System: {platform.system()} {platform.release()} ({platform.version()})")
print(f"Processor: {platform.processor()}")
print(f"CPU Cores: {psutil.cpu_count(logical=True) + psutil.cpu_count(logical=False)}")
memory_info = psutil.virtual_memory()
print(f"Total RAM: {memory_info.total / (1024**3):.2f} GB")
print()

array_length_5 = [random.randint(0, 1000) for _ in range(5)]
print(f"For Array Length {len(array_length_5)}")
print(f"Original Array: {str(array_length_5)}")
start = timeit.default_timer()
print(f"Sorted Array: {str(insertionSort(array_length_5, len(array_length_5)))} within a time of {(timeit.default_timer() - start) * 1000:.2f} milliseconds\n")
print()

array_length_10 = [random.randint(0, 1000) for _ in range(10)]
print(f"For Array Length {len(array_length_10)}")
print(f"Original Array: {str(array_length_10)}")
start = timeit.default_timer()
print(f"Sorted Array: {str(insertionSort(array_length_10, len(array_length_10)))} within a time of {(timeit.default_timer() - start) * 1000:.2f} milliseconds\n")
print()

array_length_20 = [random.randint(0, 1000) for _ in range(20)]
print(f"For Array Length {len(array_length_20)}")
print(f"Original Array: {str(array_length_20)}")
start = timeit.default_timer()
print(f"Sorted Array: {str(insertionSort(array_length_20, len(array_length_20)))} within a time of {(timeit.default_timer() - start) * 1000:.2f} milliseconds")
print()

array_length_100 = [random.randint(0, 1000) for _ in range(100)]
print(f"For Array Length {len(array_length_100)}")
print(f"Original Array: {str(array_length_100)}")
start = timeit.default_timer()
print(f"Sorted Array: {str(insertionSort(array_length_100, len(array_length_100)))} within a time of {(timeit.default_timer() - start) * 1000:.2f} milliseconds")
print()

array_length_500 = [random.randint(0, 1000) for _ in range(500)]
print(f"For Array Length {len(array_length_500)}")
print(f"Original Array: {str(array_length_500)}")
start = timeit.default_timer()
print(f"Sorted Array: {str(insertionSort(array_length_500, len(array_length_500)))} within a time of {(timeit.default_timer() - start) * 1000:.2f} milliseconds")
print()

array_length_1000 = [random.randint(0, 1000) for _ in range(1000)]
print(f"For Array Length {len(array_length_1000)}")
print(f"Original Array: {str(array_length_1000)}")
start = timeit.default_timer()
print(f"Sorted Array: {str(insertionSort(array_length_1000, len(array_length_1000)))} within a time of {(timeit.default_timer() - start) * 1000:.2f} milliseconds")