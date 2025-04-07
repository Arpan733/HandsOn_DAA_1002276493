class DynamicArray:
    def __init__(self, initial_capacity=2):
        self.capacity = initial_capacity
        self.size = 0
        self.arr = [0] * self.capacity

    def add(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        self.arr[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            print("Index out of bounds")
            return
        
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i - 1]
        
        self.arr[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            print("Index out of bounds")
            return
        
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        
        self.size -= 1
        
        if self.size <= self.capacity // 4 and self.capacity > 2:
            self._resize(max(self.capacity // 2, 2))

    def remove(self):
        if self.size > 0:
            self.size -= 1
        
            if self.size <= self.capacity // 4 and self.capacity > 2:
                self._resize(max(self.capacity // 2, 2))
                
        else:
            print("Array is already empty")
            return

    def get(self, index):
        if index < 0 or index >= self.size:
            print("Index out of bounds")
            return
        
        return self.arr[index]

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def _resize(self, new_capacity):
        new_arr = [0] * new_capacity
        
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr
        self.capacity = new_capacity

    def __str__(self):
        return "[" + ", ".join(str(self.arr[i]) for i in range(self.size)) + "]"


dyn_arr = DynamicArray()
dyn_arr.add(1)
dyn_arr.add(2)
dyn_arr.add(3)
dyn_arr.add(4)

print("Elements of the array:", dyn_arr)
print("Size of the array:", dyn_arr.get_size())
print("Capacity of the array:", dyn_arr.get_capacity())

dyn_arr.insert(2, 2)
print("\nAfter inserting 2 at index 2:", dyn_arr)

dyn_arr.delete(2)
print("\nAfter deleting element at index 2:", dyn_arr)

dyn_arr.remove()
print("\nAfter removing last element")
print("Elements of the array:", dyn_arr)
print("Size of the array:", dyn_arr.get_size())
print("Capacity of the array:", dyn_arr.get_capacity())
print()

dyn_arr.remove()
dyn_arr.remove()
dyn_arr.remove()
dyn_arr.remove()

print("\nAfter removing all elements")
print("Elements of the array:", dyn_arr)
print("Size of the array:", dyn_arr.get_size())
print("Capacity of the array:", dyn_arr.get_capacity())