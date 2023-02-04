# The max_min_diff() function is implemented:
# def max_min_diff(numbers):
#     return max(numbers) - min(numbers)
# Modify the max_min_diff() function implementation. Using the assert statement inside this function, add the ability to check the length of the numbers argument before returning the result. If the length of the numbers object is 0, raise an AssertionError without any message. Otherwise, return a valid result.

def max_min_diff(numbers):
    assert len(numbers) != 0
    return max(numbers) - min(numbers)
 
max_min_diff([])