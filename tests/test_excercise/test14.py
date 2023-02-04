# The following calculate_tax() function is implemented in a file named tax.py:
# def calculate_tax(amount, age, tax=17.0):
#     """The function returns the amount of income tax."""
 
#     tax_rate = tax / 100.0
 
#     if age <= 18:
#         return int(min(amount * tax_rate, 6000))
#     elif age <= 65:
#         return int(amount * tax_rate)
#     else:
#         return int(min(amount * tax_rate, 9000))
# The calculate_tax() function has been imported into the solution file exercise.py. Create a TestCalculateTax class that extends from unittest.TestCase and implements the following tests:
# test_tax_with_eighteen_age() checks if for 60000 and age 18 the calculated tax will be 6000
# test_tax_with_nineteen_age() checks if for 60000 and age 19 the calculated tax will be 10200
# test_tax_with_sixty_five_age() checks if for an amount of 60000 and age 65 the calculated tax will be 10200
# test_tax_with_sixty_six_age() checks if for an amount of 60000 and age 66 the calculated tax will be 9000
# Assume the default income tax rate of 17%.

def calculate_tax(amount, age, tax=17.0):
    """The function returns the amount of income tax."""
 
    tax_rate = tax / 100.0
 
    if age <= 18:
        return int(min(amount * tax_rate, 6000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 9000))

import unittest

class TestCalculateTax(unittest.TestCase):
    def test_tax_with_eighteen_age(self):
        self.assertEqual(6000, calculate_tax(60000, 18))
    def test_tax_with_nineteen_age(self):
        self.assertEqual(10200, calculate_tax(60000,19))
    def test_tax_with_sixty_five_age(self):
        self.assertEqual(10200, calculate_tax(60000,65))
    def test_tax_with_sixty_six_age(self):
        self.assertEqual(9000, calculate_tax(60000, 66))