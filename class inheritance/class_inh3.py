# Inheriting from the built-in dict class, create a class called IntDict that will only add pairs whose value is an int object to the dictionary. If you try to add a value for a key other than int, raise a TypeError with the message:
# 'The value must be an integer.'


class IntDict(dict):
    def __setitem__(self,key, value):
        if isinstance(value, int):
            return dict.__setitem__(self, key, value)
        else:
            raise TypeError ("The value must be an integer.")
