# Implement a function called calculate() that will return all three-digit palindromic numbers in both decimal and binary notation. In response, call the calculate() function and print the result to the console.

def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        bin_number  = str(bin(number))[2:]
        if bin_number == bin_number[::-1]:
            return True
    else:
        return False

def calculate():
    list_of_nums= []
    for i in range(100,1000):
        if is_palindrome(i):
            list_of_nums.append(i)
        else:
            continue
    return list_of_nums


print(calculate())