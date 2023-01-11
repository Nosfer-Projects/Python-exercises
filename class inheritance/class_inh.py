# Class inheritance issues. Consider the list built-in class. One of the methods of this class is the append() method, which adds an item to the end of the list:
# >>> help(list.append)
# Help on method_descriptor:
# append(self, object, /)Append object to the end of the list.
# An element can be, for example, an object of class int, float, str, bool, or NoneType.Inheriting from the list built-in class, create a class called IntList that will only append int objects. If you try to add an object of a different type, raise a TypeError with the message: 'The value must be an integer.'


class IntList(list):
 
    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('The value must be an integer.')
        return list.append(self, value)