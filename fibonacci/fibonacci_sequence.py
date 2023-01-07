# Consider the Fibonacci sequence. It is a sequence of natural numbers defined recursively as follows:
# the first term of the sequence is 0
# the second term of the sequence is 1
# each term of the sequence is the sum of the previous two
# Some beginning words of the sequence:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# Find the sum of all even terms of the Fibonacci sequence with values ​​less than 1,000,000 (1 million).
# Present the solution in the form of a function called calculate(). In response, call the calculate() function and print the result to the console.



def calculate():
    total = 0
    a= 0
    b= 1
    while a < 1000000:
            if a % 2 ==0:
                total += a
            a,b = b,a+b
    return total

print(calculate())