# A fragment of a class called Matrix has been implemented, which will provide an interface for working with matrices.
# Add a method called identity() to the Matrix class to return the identity matrix for square matrices. If the matrix is ​​not a square matrix, the method is expected to return None.
# Reminder: The identity matrix on the main diagonal has all ones and the rest is filled with zeros


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
                type(number) in (int, float)
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

    @property
    def n_rows(self):
        return len(self.array)

    @property
    def n_cols(self):
        if len(self.array) == 0:
            return 0
        return len(self.array[0])

    @property
    def size(self):
        return self.n_rows, self.n_cols

    @property
    def is_square_matrix(self):
        return self.size[0] == self.size[1]

    def zero(self):
        array = [
            [0 for _ in range(self.n_cols)]
            for _ in range(self.n_rows)
        ]
        return Matrix(array)

    def identity(self):
        if self.n_rows and self.n_cols == 0:
            return None
        elif self.n_rows == self.n_cols:
            array = []
            idx = 0
            for x in range (self.n_rows):
                ar = []
                for i in range (self.n_cols):
                    if i == idx:
                        ar.append(1)
                    else:
                        ar.append(0)
                array.append(ar)
                idx +=1

            return array


m = Matrix([[3, 1, 6]])
print(m.identity())

