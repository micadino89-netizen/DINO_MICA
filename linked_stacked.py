class LinkedStack:
    def __init__(self):
        self.top = None                

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False                    

    def push(self, value):
        node = Node(value)
        node.next = self.top           
        self.top = node                

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.top.value
        self.top = self.top.next        
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek")
        return self.top.value

    def to_list(self):
        """Elements from top to bottom (for display only)."""
        items, cur = [], self.top
        while cur is not None:
            items.append(cur.value)
            cur = cur.next
        return items
