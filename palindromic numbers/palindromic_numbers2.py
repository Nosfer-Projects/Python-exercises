# Implement a function that will return the largest palindromic number resulting from the product of two-digit numbers.

def palin_num2():
    numbers = []
    for i in range(10, 100):
        for j in range(10, 100):
            numbers.append(i * j)
    numbers.sort(reverse=True)
    for num in numbers:
        if str(num ) == str(num )[::-1]:
            return num 

print(palin_num2())