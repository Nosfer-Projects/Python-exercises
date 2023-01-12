# In the __init__() method, do some pre-validation before setting the array instance attribute:
# check if the passed argument is an instance of the list class, if not raise a TypeError with the message:
# 'To create a matrix you need to pass a nested list of values.'
# check if passed list contains any element, if not set array instance attribute value to empty list[]
# check if all elements of passed list are list objects, if not raise TypeError with message:
# 'Each element of the array (nested list) must be a list.'
# check if all lists of passed nested list are same length (do columns have same number of elements) if not raise TypeError with message:
# 'All columns must be the same length.'
# check if all elements passed to create matrix are int or float class objects, if not raise TypeError with message:
# 'The values ​​must be of type int or float.'


class Matrix:
 
    def __init__(self, array):
 
        if not isinstance(array, list):
            raise TypeError(
                'To create a matrix you need to pass a nested '
                'list of values.'
            )
 
        if len(array) != 0:
            if not all(isinstance(row, list) for row in array):
                raise TypeError(
                    'Each element of the array (nested list) must '
                    'be a list.'
                )
 
            if not all(len(row) for row in array):
                raise TypeError(
                    'Columns must contain at least one item.'
                )
 
            column_length = len(array[0])
 
            if not all(
                len(row) == column_length for row in array
            ):
                raise TypeError(
                    'All columns must be the same length.'
                )
 
            if not all(
                isinstance(number, (int, float))
                for row in array
                for number in row
            ):
                raise TypeError(
                    'The values must be of type int or float.'
                )
 
            self.array = array
 
        else:
            self.array = []
 
    def __repr__(self):
        return str(self.array)


a = Matrix([[5]])
print(a)