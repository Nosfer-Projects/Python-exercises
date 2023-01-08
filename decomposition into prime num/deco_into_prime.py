# The decomposition of a number based on the first is to determine the natural number by the product of the initial number.
# Implement a function that takes a natural number as an argument and returns a list containing the prime factorization of that number. Present the solution in the form of a function called calculate(). Do not perform any validation on the argument passed to the function.


def calculate(number):
    i = 2
    factors = []
    while i * i <= number:
        if not number % i == 0:
            i += 1
        else:
            number = number // i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

print(calculate(48))