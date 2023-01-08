# The algorithm goes from left to right through the individual digits and returns a list of two-element tuples. Each tupla consists of a digit and the number of repetitions of that digit until the next, different digit in the number is encountered.
# example :111155522500 -> [('1', 4), ('5', 3), ('2', 2), ('5', 1), ('0', 2)]
# Implement a function called compress() that will compress the number as described above.


from itertools import groupby
 
 
def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, len(list(group))))
    return result


print(compress(1000040000))
