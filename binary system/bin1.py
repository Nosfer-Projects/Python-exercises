# How to easily convert a decimal number to binary?
# You can use a simple algorithm:
# Find the remainder when a number is divided by 2 (this will be the first number on the right in binary)
# Divide a number by 2 using integer division - //
# Repeat the above steps until the number is greater than 0.

def decimal_to_binary(number):
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        result += str(number % 2)
        number = number // 2
    return result[::-1]