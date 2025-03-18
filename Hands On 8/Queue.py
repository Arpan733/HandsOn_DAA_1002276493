class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.is_full():
            print("Queue Overflow!")
            return
        
        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return value

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow!")
            return
        
        value = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        return value

    def front_value(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            print("Queue is Empty!")
            return
        
        print("Queue: ", end="")

        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        
        print()


queue = Queue(5)
print(f"Queue Enqueue: {queue.enqueue(1)}")
print(f"Queue Enqueue: {queue.enqueue(2)}")
print(f"Queue Enqueue: {queue.enqueue(3)}")
print(f"Queue Enqueue: {queue.enqueue(4)}")
queue.display()
print(f"Queue Front: {queue.front_value()}")
print(f"Queue Dequeue: {queue.dequeue()}")
queue.display()
print(f"Queue Enqueue: {queue.enqueue(5)}")
queue.display()
print(f"Queue Front: {queue.front_value()}")
print(f"Queue Dequeue: {queue.dequeue()}")
print(f"Queue Dequeue: {queue.dequeue()}")
print(f"Queue Dequeue: {queue.dequeue()}")
print(f"Queue Dequeue: {queue.dequeue()}")
queue.display()