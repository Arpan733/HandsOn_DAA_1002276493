# Leverage your implementation of quicksort to implement the ith order statistic.
# Demonstrate it's working via an example.
# Upload your code to github.

import random

def quicksort(arr, low, high, i):
    if low == high:
        return arr[low]
    
    pivot = arr[high]
    index = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[index], arr[j] = arr[j], arr[index]
            index += 1
    
    arr[index], arr[high] = arr[high], arr[index]
    pivot_index = index
    k = pivot_index - low + 1

    if i == k:  
        return arr[pivot_index]
    elif i < k:
        return quicksort(arr, low, pivot_index - 1, i)
    else:
        return quicksort(arr, pivot_index + 1, high, i - k)

arr = [random.randint(0, 100) for _ in range(10)]
i = random.randint(0, 10)

print(f"The array is: {str(arr)}")
print(f"The value of i is: {i}")

result = quicksort(arr, 0, len(arr) - 1, i)

print(f"The {i}th smallest element is: {result}")
