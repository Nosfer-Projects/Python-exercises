# Implement a function called is_prime() that takes a natural number as an argument and checks if it is a prime number. In the case of a prime number, the function is to return a logical value True, otherwise False.

def is_prime(number):
    if number < 2:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True


print(is_prime(2))
