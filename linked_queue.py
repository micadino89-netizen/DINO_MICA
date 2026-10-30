class LinkedQueue:
    def __init__(self):
        self.front = None               
        self.rear = None                

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False                    

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node         
        else:
            self.rear.next = node       
        self.rear = node                

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:        
            self.rear = None           
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: nothing to peek")
        return self.front.value

    def to_list(self):
        """Elements from front to rear (for display only)."""
        items, cur = [], self.front
        while cur is not None:
            items.append(cur.value)
            cur = cur.next
        return items
