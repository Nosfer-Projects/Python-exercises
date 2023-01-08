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