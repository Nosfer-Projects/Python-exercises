# In summary, we reduce an iterable object to some final value using a reducing function. There are three steps in this process:
# Calling the function on the first two elements of the iterable and generating a partial result
# Calling a function on a partial result and the next element of an iterable object
# Repeating the process until the elements in the iterable are exhausted and returning the result
# Convert the reduce() function from the previous exercise into a function called reduce_with_start() so that it takes a third argument called start, which will be the starting value in the iterable reduction process.



def reduce_with_start(function, iterable, start):
    if len(iterable) == 0:
        if start == None:
            return None
        else:
            return start
    result = start
    for item in iterable:
        result = function(result, item)
    return result


print(reduce_with_start(lambda x, y: x + y, [1,2,3], 100))