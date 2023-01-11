# In summary, we reduce an iterable object to some final value using a reducing function. There are three steps in this process:
# Calling the function on the first two elements of the iterable and generating a partial result
# Calling a function on a partial result and the next element of an iterable object
# Repeating the process until the elements in the iterable are exhausted and returning the result
# Implement a function called reduce() that takes two arguments:
# function - function used to reduce the iterable object
# iterable - iterable object
# and will reduce the passed iterable object (iterable) with the passed function function. If an empty iterable is passed, the function is expected to return None.

def reduce(function, iterable):
    if len(iterable) == 0:
        return None
    result = iterable[0]
    for item in iterable[1:]:
        result = function(result, item)
    return result

print(reduce(lambda x, y: x + y, ['p', 'y', 't', 'h', 'o', 'n']))