# Our task in this exercise will be to implement a class called Queue, which will represent the queue in the simplest way. Required queue operations (class methods) that we need to implement:
# enqueue(item) -> put item item at the end of the queue
# dequeue() -> remove and return the element from the top of the queue; if the queue is empty, raise an IndexError with the message: 'The queue is empty.'
# In addition to the operations described above, add implementations of two special methods:
# __init__() -> setting a protected attribute called _data that will store the queue items as a list
# __len__() -> defining the action of the built-in function len() -> number of queue elements.

class Queue():
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def enqueue(self, item):
        self._data.append(item)
    def dequeue(self):
        if len(self._data) == 0:
            raise IndexError ("The queue is empty.")
        else:
            return self._data.pop(0)