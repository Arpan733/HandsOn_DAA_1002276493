# problem 2
# Given a sorted array array of size N, the task is to remove the duplicate elements from the array.

# Examples: 

# Input: array = [2, 2, 2, 2, 2]
# Output: array= [2]
# Explanation: All the elements are 2, So only keep one instance of 2.

# Input: array = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# Output: array[] = {1, 2, 3, 4, 5}

# Note, you can't use something like the set container in C++.

print(f"Enter the elements of array (space-separated):")
array = list(map(int, input().split()))
index = 0

while index < len(array) and index + 1 < len(array):
    if array[index] == array[index + 1]:
        array.remove(array[index + 1])
    else:
        index += 1

print(f"Duplicate removed array: {array}")