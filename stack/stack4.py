# A class called Stack is implemented, which is the simplest representation of a stack.
# Add a method called top() to the Stack class to read the item at the top of the stack (without removing the item from the stack). For an empty stack, raise an EmptyStackError with the message: 'The stack is empty.'


class EmptyStackError(Exception):
    pass


class Stack:
    """The simplest stack."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data[-1]