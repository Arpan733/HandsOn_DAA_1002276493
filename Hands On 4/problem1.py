# Problem 1
# Given K sorted arrays of size N each, the task is to merge them all maintaining their sorted order.

# Examples: 

# Input: K = 3, N =  4
# array1 = [1,3,5,7]
# array2 = [2,4,6,8]
# array3 = [0,9,10,11]
# Output: [0,1,2,3,4,5,6,7,8,9,10,11]
# Merged array in a sorted order where every element is greater than the previous element.

# Input: K = 3, N =  3
# array1 = [1,3,7]
# array2 = [2,4,8]
# array3 = [9,10,11]
# Output: [1,2,3,4,7,8,9,10,11]
# Merged array in a sorted order where every element is greater than the previous element.

k = int(input("Enter the number of arrays (k): "))
n = int(input("Enter the size of array (n): "))
arr = []

for i in range(k):
    print(f"Enter the elements of array {i + 1} (space-separated):")
    array = list(map(int, input().split()))
    while len(array) != n:
        print(f"Error: The array must contain exactly {n} elements. Please enter the array again.")
        print(f"Enter the elements of array {i + 1} (space-separated):")
        array = list(map(int, input().split()))
        continue
    
    arr.append(array)

index = [0] * k
result = []

while len(result) != n * k:
    min = 100000
    ind = 0

    for i in range(len(index)):
        if index[i] < n and min > arr[i][index[i]]:
            min = arr[i][index[i]]
            ind = i
        
    result.append(min)
    index[ind] = index[ind] + 1

print(f"Merged array in sorted order is: {result}")
