class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


queue = Queue()
print("Queue is empty:", queue.is_empty())  
queue.enqueue("Superior")
queue.enqueue("Usman")
queue.enqueue("Aliza")
print("Front item:", queue.peek())  
print("Dequeued item:", queue.dequeue())  
print("Queue is empty:", queue.is_empty())  
print("Dequeued item:", queue.dequeue())  
print("Dequeued item:", queue.dequeue())  
print("Queue is empty:", queue.is_empty())  
