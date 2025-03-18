class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity
        self.size = 0

    def insert_at_head(self, value):
        if self.size == self.capacity:
            print("Linked List Overflow!")
            return

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

        return value

    def remove_from_head(self):
        if self.head is None:
            print("Linked List Underflow!")
            return

        removed_value = self.head.value
        self.head = self.head.next
        self.size -= 1

        return removed_value

    def top(self):
        if self.head is None:
            print("Linked List is Empty!")
            return

        return self.head.value
    
    def display(self):
        if self.head == -1:
            print("Linked List is Empty!")
            return

        current = self.head
        print("Linked List:", end=" -> ")

        while current:
            print(current.value, end=" -> ")
            current = current.next
        
        print()


linked_list = SinglyLinkedList(5)
print(f"Insert at Head: {linked_list.insert_at_head(1)}")
print(f"Insert at Head: {linked_list.insert_at_head(2)}")
print(f"Insert at Head: {linked_list.insert_at_head(3)}")
print(f"Insert at Head: {linked_list.insert_at_head(4)}")
linked_list.display()
print(f"Top Element: {linked_list.top()}")
print(f"Remove from Head: {linked_list.remove_from_head()}")
linked_list.display()
print(f"Insert at Head: {linked_list.insert_at_head(4)}")
print(f"Insert at Head: {linked_list.insert_at_head(5)}")
print(f"Insert at Head: {linked_list.insert_at_head(6)}")
linked_list.display()
print(f"Top Element: {linked_list.top()}")
print(f"Remove from Head: {linked_list.remove_from_head()}")
print(f"Remove from Head: {linked_list.remove_from_head()}")
print(f"Remove from Head: {linked_list.remove_from_head()}")
print(f"Remove from Head: {linked_list.remove_from_head()}")
print(f"Remove from Head: {linked_list.remove_from_head()}")
print(f"Remove from Head: {linked_list.remove_from_head()}")
linked_list.display()