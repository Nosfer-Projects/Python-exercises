# Implement a function called is_valid_html() that checks whether the passed expression (in the form of a str object) is valid in terms of the number of open and closed HTML tags.
# The function is supposed to return the logical value True when the submitted HTML document is correct, on the contrary False. The function takes one argument. We omit validation, we assume that the user passes an object of type str.

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

    def is_valid_html(html):
        stack = Stack()
        first_char_idx = html.find('<')
        while first_char_idx != -1:
            next_char_idx = html.find('>', first_char_idx + 1)
            if next_char_idx == -1:
                return False
            tag = html[first_char_idx + 1: next_char_idx]
            if not tag.startswith('/'):
                stack.push(tag)
            else:
                if stack.is_empty():
                    return False
                if tag[1:] != stack.pop():
                    return False
            first_char_idx = html.find('<', next_char_idx + 1)
        return stack.is_empty()