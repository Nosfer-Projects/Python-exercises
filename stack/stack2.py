# A class called Stack is implemented, which is the simplest representation of a stack.
# Add a method called is_empty() to the Stack class to check if the stack is empty. In the case of an empty stack, the method is to return the logical value True, otherwise False. Also modify the pop() method using the implemented is_empty() method in the defined conditional statement.




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
        if  self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data.pop()
    
    def is_empty(self):
        if len(self._data) == 0:
            return True
        return False