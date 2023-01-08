# Consider the following problem. We have an application in which at some point of operation we get a matrix in the form of a string (an object of type str). For example, the following string:
# string = """4 2 7
# 1 5 4
# 2 6 8"""
# will represent a 3x3 matrix. Each row of the matrix is ​​written on a separate line. Each row element is separated from the other element by a space.
# On such a matrix in the form of a string, it's hard to work and perform some additional operations. We will transform such a matrix into nested lists. And so for the above case it will be a list:
# [[4, 2, 7], [1, 5, 4], [2, 6, 8]]

class Matrix():
    def __init__(self,main_string):
        self.main_string= main_string
    
    def matrix(self):
        m= []
        for i in self.main_string.split("\n"):

            list_nums = [int(num) for num in i.split()]
            m.append(list_nums)
        return m
matrix = Matrix('1')
print(matrix.matrix())
