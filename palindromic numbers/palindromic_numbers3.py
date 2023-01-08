# Implement a function called is_palindrome() that checks whether the given number is palindromic in both decimal and binary notation.

def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        bin_number  = str(bin(number))[2:]
        if bin_number == bin_number[::-1]:
            return True
    else:
        return False

print(is_palindrome(99))