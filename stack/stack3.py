# Implement a function called is_palindrome() that checks if the text passed is a palindrome. A palindrome is a phrase that reads the same from left to right and right to left.
# The function is to return True if the given expression is a palindrome, False on the contrary. The function takes one argument. We omit validation, we assume that the user passes an object of type str.
# When implementing the function, consider how you can solve this problem using the stack. For this purpose, use the Stack class.


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

    def is_palindrome(self, text):
        self._data.append(text)
        if self._data[0] == self._data[0][::-1]:
            return True
        return False

a = Stack()
print(a.is_palindrome("obo"))

