class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    def push(self,item):
        return self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.item)

test = Stack()
test.isEmpty()
test.push('hello')
test.push(4.6)
test.push(45)
print(test.peek())
print(test.pop())
print(test.isEmpty())