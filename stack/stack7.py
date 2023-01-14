# Implement a function called transfer() that transfers all the elements of the first stack to the second stack so that the element on top of the first stack is the first element inserted into the second stack.
# The transfer() function is supposed to take two arguments:
# stack_1 - the first stack from which we transfer elements
# stack_2 - the second stack to which we transfer elements
# and return the given stacks.

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

def transfer(stack_1, stack_2):
    while not stack_1.is_empty():
        stack_2.push(stack_1.pop())
    return stack_1, stack_2
