# Suppose we have a problem to solve that requires us to use a list, and we don't want to allow users to add items of different types to the list. We would like to limit this operation to natural numbers only. For the purposes of the solution, we do not consider 0 to be a natural number.
# Inheriting from the list built-in class, create a class called NaturalList that will allow append() to add only natural numbers, that is, int objects that are greater than zero. If you try to add an object of a different type, raise a TypeError with the message:
# 'The value must be an integer.'
# If you try to add a number that is not a natural number, raise a ValueError with the message:
# 'The value must be a natural number.'




class NaturalList(list):
 
    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('The value must be an integer.')
        if value <= 0:
            raise ValueError ("The value must be a natural number.")
        return list.append(self, value)