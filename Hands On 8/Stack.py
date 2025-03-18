class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.topIndex = -1

    def is_empty(self):
        return self.topIndex == -1

    def is_full(self):
        return self.topIndex == self.size - 1

    def push(self, value):
        if self.is_full():
            print("Stack Overflow!")
            return
        
        self.topIndex += 1
        self.stack[self.topIndex] = value
        return value

    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
            return
        
        value = self.stack[self.topIndex]
        self.stack[self.topIndex] = None
        self.topIndex -= 1
        return value

    def top(self):
        if self.is_empty():
            print("Stack is Empty!")
            return
        
        return self.stack[self.topIndex]
    
    def display(self):
        if self.is_empty():
            print("Stack is Empty!")
            return
        
        print("Stack: ", end="")

        for i in self.stack:
            print(i, end=" ")
        
        print()


stack = Stack(5)
print(f"Stack Top: {stack.top()}")
print(f"Stack Push: {stack.push(1)}")
print(f"Stack Push: {stack.push(2)}")
print(f"Stack Push: {stack.push(3)}")
print(f"Stack Push: {stack.push(4)}")
stack.display()
print(f"Stack Top: {stack.top()}")
print(f"Stack Pop: {stack.pop()}")
stack.display()
print(f"Stack Push: {stack.push(4)}")
print(f"Stack Push: {stack.push(5)}")
print(f"Stack Push: {stack.push(6)}")
stack.display()
print(f"Stack Top: {stack.top()}")
print(f"Stack Pop: {stack.pop()}")
print(f"Stack Pop: {stack.pop()}")
print(f"Stack Pop: {stack.pop()}")
print(f"Stack Pop: {stack.pop()}")
print(f"Stack Pop: {stack.pop()}")
print(f"Stack Pop: {stack.pop()}")
stack.display()