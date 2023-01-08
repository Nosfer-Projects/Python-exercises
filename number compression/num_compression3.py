# The algorithm goes from left to right through the individual digits and returns an object of type str. Each digit encountered is recorded along with the number of repetitions of that digit with dots until the next, different digit in the number is encountered.
# 111155522500 -> '1....5...2..5.0..'
# Implement a function called compress() that will compress the number as described above.
from itertools import groupby

def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group))*".")))
    result = [''.join(item) for item in result]
    return ''.join(result)


print(compress(111155522500))