class ArrayStack:
    def __init__(self, capacity):
        self.data = [None] * capacity  
        self.top = -1                  

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push to a full stack")
        self.top = self.top + 1        
        self.data[self.top] = value    

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.data[self.top]    
        self.top = self.top - 1        
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek")
        return self.data[self.top]

    def to_list(self):
        """Elements from top to bottom (for display only)."""
        return [self.data[i] for i in range(self.top, -1, -1)]
            
