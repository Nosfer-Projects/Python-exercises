# The algorithm goes from left to right through each digit and returns an object of type str. Each digit encountered is stored along with the number of repetitions of that digit until the next, different digit in the number is encountered. Each encountered digit along with the number of repetitions is separated by a '_' character.

# Implement a function called compress() that will compress the number as described above.

from itertools import groupby
 
 
def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)


print(compress(111155522500))