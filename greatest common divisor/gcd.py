# Implement a function called greatest_common_divisor() that will find the greatest common divisor of two numbers

def gcd(num1, num2):
    divisor1= []
    divisor2 = []
    for i in range(1, num1+1):
        if num1 % i == 0:
            divisor1.append(i)
    for i in range(1, num2+1):
        if num2 % i == 0:
            divisor2.append(i)
    final_numbers = [x for x in divisor1 if x in divisor2]
    return max(final_numbers)

print(gcd(32,48))