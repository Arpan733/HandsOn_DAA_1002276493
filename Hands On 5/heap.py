# Min-Heap

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return (i * 2) + 1

    def right(self, i):
        return (i * 2) + 2

    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def build_min_heap(self, arr):
        self.heap = arr

        for i in range(len(arr) // 2 - 1, -1, -1):
            self.heapify(i)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        if self.heap:
            self.heapify(0)

        return root

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def display(self):
        print(self.heap)


if __name__ == "__main__":
    heap = MinHeap()

    print("Welcome to Min-Heap Operations!!")
    while True:
        print("\nChoose an operation which you want to perform:")
        print("1. Build Min-Heap from an array")
        print("2. Insert an element into the heap")
        print("3. Pop the root element from the heap")
        print("4. Display the heap")
        print("5. Exit")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            arr = list(map(float, input("Enter the array elements(separated by spaces): ").split()))
            heap.build_min_heap(arr)
            print("Min-Heap built successfully!")
            heap.display()
        elif choice == 2:
            element = float(input("Enter the element to insert into the heap: "))
            heap.insert(element)
            print(f"Inserted {element} into the heap.")
            heap.display()
        elif choice == 3:
            if len(heap.heap) == 0:
                print("Heap is empty!")
            else:
                popped = heap.pop()
                print(f"Popped element: {popped}")
                heap.display()
        elif choice == 4:
            print("Current Min-Heap:")
            heap.display()
        elif choice == 5:
            print("Exit!!")
            break
        else:
            print("Choose the number based on it's corresponding operation!\nPlease try again.")
