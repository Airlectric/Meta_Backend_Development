class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


# #test

# myLine = Queue()

# myLine.enqueue('baseball')
# myLine.enqueue(4)
# myLine.enqueue(4.2)

# print(myLine.size())
# print(myLine.isEmpty())
# print(myLine.dequeue())

# q = Queue()
# q.enqueue('hello')
# q.enqueue('dog')
# q.enqueue(3)
# q.dequeue()

# print(q.dequeue())
# print(q.dequeue())