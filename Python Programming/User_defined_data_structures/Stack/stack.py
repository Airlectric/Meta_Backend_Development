class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

# #testing

# stack = Stack()

# stack.push(4)
# stack.push('Dairy')
# stack.push(True)

# print('Top element:', stack.peek())

# print('Popped:', stack.pop())
# print('Popped:', stack.pop())

# print('Is it empty :', stack.isEmpty())


