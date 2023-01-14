# Create an instance of the Queue class and perform the following operations in the given order:
# add item '529' to queue
# add item '623' to queue
# dequeue an item
# add item '532' to queue
# display the first item in the queue
# add item '304' to queue
# dequeue an item
# In response, print the number of items left in the queue.

class Queue:
    """The simplest queue."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('The queue is empty.')
        return self._data.pop(0)
    
    def is_empty(self):
        if len(self._data) == 0:
            return True
        return False
    def first(self):
        if self.is_empty():
            raise IndexError('The queue is empty.')
        return self._data[0]

q = Queue()
q.enqueue("529")
q.enqueue("623")
q.dequeue()
q.enqueue("532")
q.first()
q.enqueue("304")
q.dequeue()
print(len(q))