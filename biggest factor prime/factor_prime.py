# Factoring a number into prime factors consists in writing any natural number as a product of prime numbers
# A number that is greater than 1 and is not prime is called a composite number.
# return the greatest prime factor of that number. Present the solution in the form of a function called calculate().

def calculate(number):
    i = 2
    factor = []
    while i*i <= number:
        if number % i != 0:
            i += 1
        else:
            number = number // i
            factor.append(i)
    if number > 1:
        factor.append(number)
    return max(factor)

print(calculate(15)) 