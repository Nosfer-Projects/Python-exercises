#All natural numbers (except natural for the purpose of zero problems) divisible by 5 or 7 less than 20 are: [0, 5, 7, 10, 14, 15]. The sum of these numbers is: 51.
# Find the sum of all numbers divisible by 5 or 7 less than 100.
# Present the solution in a function called calculate(). In response to the query compute() and print the result to the console.


def calculate():
    sum = 0
    for i in range(100):
        if i % 5 == 0 or i % 7 == 0:
            sum += i
    return sum

print(calculate())