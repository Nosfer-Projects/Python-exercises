# In the solution file called exercise.py, import the income_tax() function from the tax module. Create a TestIncomeTax class that extends from unittest.TestCase and implements the following tests:
# test_tax_below_threshold() checks if for 60000 the calculated tax will be 10200
# test_tax_equal_threshold() checks if for the amount 85528 ​​the calculated tax will be 14539.76
# test_tax_above_threshold() checks if for an amount of 100000 and age 65 the calculated tax will be 19170.8


def income_tax(income, first_thresh=17.0, second_thresh=32.0):
    first_rate = first_thresh / 100.0
    second_rate = second_thresh / 100.0
    threshold = 85528
    if income < threshold:
        return income * first_rate
    else:
        return threshold * first_rate + (income - threshold) * second_rate


from unittest import TestCase

class TestIncomeTax(TestCase):
    def test_tax_below_threshold(self):
        self.assertEqual(10200, income_tax(60000))
    def test_tax_equal_threshold(self):
        self.assertAlmostEqual(14539.76, income_tax(85528), 2)
    def test_tax_above_threshold(self):
        self.assertAlmostEqual(19170.8, income_tax(100000),1)