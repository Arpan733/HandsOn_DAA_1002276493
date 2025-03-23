# Use the multiplication AND division method for your hash function
#   Note your code should be generic enough to allow for ANY hash function
# For simplicity assume your keys are integers and the values (data) are integers
# Use collision resolution by chaining
#   Use a doubly linked list and you must write your own (so for example you can't use "list" in C++)
# You are only allowed to use C-style array's for this implementation (so for example no C++ vectors)
# Your Hash table should grow and shrink
#   When it's full double the array size and re-hash everything
#   When it's becoming empty e.g. 1/4 empty, then half the size of the array and re-hash everything

# Node for the doubly Linked List
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

# Doublt Linked List class with insert, remove, and serach functions
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove(self, key):
        current = self.head

        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                
                if current.next:
                    current.next.prev = current.prev
                
                if current == self.head:
                    self.head = current.next
                
                return True
            
            current = current.next
        
        return False

    def search(self, key):
        current = self.head

        while current:
            if current.key == key:
                return current.value
        
            current = current.next
        
        return None

    def __iter__(self):
        current = self.head
        
        while current:
            yield (current.key, current.value)
            current = current.next

# Hash Class with hash, resize, insert, remove, search, and print_table functions
class HashTable:
    def __init__(self, initial_capacity=3):
        self.capacity = initial_capacity
        self.size = 0
        self.table = [DoublyLinkedList() for _ in range(self.capacity)]
        self.A = 0.6180339887

    def hash(self, key):
        fractional = (key * self.A) % 1
        return int(self.capacity * fractional)

    def resize(self, new_capacity):
        old_table = self.table
        self.capacity = new_capacity
        self.table = [DoublyLinkedList() for _ in range(self.capacity)]
        self.size = 0

        for chain in old_table:
            for k, v in chain:
                self.insert(k, v)

    def insert(self, key, value):
        if self.size / self.capacity >= 1.0:
            self.resize(self.capacity * 2)

        index = self.hash(key)

        if self.table[index].search(key) is None:
            self.size += 1

        self.table[index].insert(key, value)

    def remove(self, key):
        index = self.hash(key)
        
        if self.table[index].remove(key):
            self.size -= 1

            if self.capacity > 3 and self.size <= self.capacity // 4:
                self.resize(max(3, self.capacity // 2))
        else:
            print(f"Key {key} not found.")

    def search(self, key):
        index = self.hash(key)
        result = self.table[index].search(key)
        return result if result is not None else -1

    def print_table(self):
        for i, chain in enumerate(self.table):
            print(f"Bucket {i}: ", end="")
            
            for k, v in chain:
                print(f"({k}, {v}) -> ", end="")
            
            print("None")

# Start Point
if __name__ == "__main__":
    ht = HashTable()
    ht.insert(10, 100)
    ht.insert(20, 200)
    ht.insert(30, 300)
    print("\nHash table with 3 elements.")
    ht.print_table()
    ht.insert(40, 400)
    print("\nHash table with 4 elements. (Expanded)")
    ht.print_table()
    print("\nSearch for key 20:", ht.search(20))
    ht.remove(20)
    ht.remove(40)
    print("\nHash table after deleting some data.")
    ht.print_table()
    ht.remove(10)
    ht.remove(30)
    print("\nHash table after deleting all data.")
    ht.print_table()
