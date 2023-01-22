# The calculate_tax() function is given (without validating the arguments):
# def calculate_tax(amount, tax_rate, age):
#     """The function returns the amount of income tax."""
 
#     if age < 18:
#         return int(min(amount * tax_rate, 5000))
#     age < 65:
#         return int(amount * tax_rate)
#     else:
#         return int(min(amount * tax_rate, 8000))
# The function is supposed to work as follows:
# for age less than or equal to 18 returns the minimum of the following two values:
# taxable amount * tax rate
# 5000
# for age over 18 and age less than or equal to 65 returns:
# taxable amount * tax rate
# for age over 65 returns the minimum of the following two values:
# taxable amount * tax rate
# 8000
# There are two errors in the calculate_tax() function you provided. Try to improve the implementation of this function so that the function passes the tests implemented in the test_calculate_tax() function.
# The test_calculate_tax() function asserts the following test cases:
# calculate_tax(60000, 0.15, 10) == 5000
# calculate_tax(60000, 0.15, 18) == 5000
# calculate_tax(60000, 0.15, 19) == 9000
# calculate_tax(60000, 0.15, 65) == 9000
# calculate_tax(60000, 0.15, 66) == 8000


def calculate_tax(amount, tax_rate, age):
    """The function returns the amount of income tax."""

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))

def test_calculate_tax():
    assert calculate_tax(60000, 0.15, 10) == 5000        
    assert calculate_tax(60000, 0.15, 18) == 5000
    assert calculate_tax(60000, 0.15, 19) == 9000
    assert calculate_tax(60000, 0.15, 65) == 9000
    assert calculate_tax(60000, 0.15, 66) == 8000

test_calculate_tax()