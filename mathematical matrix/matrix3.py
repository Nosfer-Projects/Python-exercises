# You just need to implement the column() method. Proof tests run several test cases to validate the solution.

class Matrix:
    """Simple Matrix class."""

    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]

    def __repr__(self):
        return '\n'.join([(' '.join([str(i) for i in row])) for row in self.matrix])
    
    def row(self,number):
        return self.matrix[number]

    def column(self, number):
        return [x[number] for x in self.matrix]

matrix= Matrix('3 4\n5 6')
print(matrix.column(0))