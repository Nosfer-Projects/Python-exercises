# Modify the max_min_diff() function implementation. Using the assert statement inside this function, add the ability to check the length of the numbers argument before calculating the result. If its length is equal to 0, raise an AssertionError with the message:



'The numbers object cannot be empty.'


def max_min_diff(numbers):
    assert len(numbers)!= 0, 'The numbers object cannot be empty.'
    return max(numbers) - min(numbers)
    
print(max_min_diff([]))