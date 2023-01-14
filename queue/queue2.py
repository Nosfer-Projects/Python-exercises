# Add two methods to the Queue class:
# method called is_empty(), which will check if the queue is empty. In the case of an empty queue, the method is to return the logical value True, otherwise False
# a method called first(), which will allow you to read the first element of the queue (without removing it)
# Also modify the dequeue() method using the implemented is_empty() method in the defined conditional statement.

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