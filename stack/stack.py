# Let's consider the basic data structure which is the stack. A stack is a data structure containing elements that are inserted and removed according to the LIFO (last-in, first-out) principle. The user can insert elements into the stack at any time, but can only access or remove the last inserted element, which remains on the so-called top of the stack.
# We can imagine a pile, for example, as a pile of books on a desk. New books are added to the top of the pile. On the other hand, if we want to take a book, we also take it from above. In this way, we remove the books from the stack in the reverse order of their position. This behavior reflects the aforementioned LIFO principle (last in, first out).
# Many algorithms use stacks. Web browsers can store the addresses of recently visited sites in a stack. Every time a user visits a new site, the address of that site is added to the address stack. The browser then allows the user to navigate back to previously visited sites with a 'Back' button (picture of an item from the stack).
# Our task in this exercise will be to implement a class called Stack, which will represent a stack in the simplest way. Required stack operations (class methods) that we need to implement:
# push(item) -> push item to the top of the stack
# pop() -> remove and return the item from the top of the stack; if the stack is empty, raise an EmptyStackError with the message: 'The stack is empty.'
# Add an error called EmptyStackError by inheriting the built-in Exception class.
# In addition to the operations described above, add implementations of two special methods:
# __init__() -> setting a protected attribute called _data that will store the stack elements as a list
# __len__() -> defining the action of the built-in function len() -> number of stack elements.




class EmptyStackError(Exception):
    pass

class Stack:
    def __init__(self):
        self._data = []
    
    def __repr__(self):
        return ' '.join(map(str, self._data))
    
    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if len(self) == 0:
            raise EmptyStackError ("This stack is empty")
        return self._data.pop()




a = Stack()
a.push("python")
a.push("sql")
print(len(a))
a.pop()
print(len(a))
a.pop()
a.pop()
