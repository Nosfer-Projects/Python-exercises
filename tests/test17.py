# The SimpleTaxCalculator class is implemented in tax.py. In the solution file called exercise.py, import the SimpleTaxCalculator class from the tax module. Next, create a TestIncomeTax class that inherits from unittest.TestCase. Add a setUpClass() class method to create an instance of the SimpleTaxCalculator class and assign it to the attribute named calc of the TestIncomeTax class (assignment at the level of the TestIncomeTax test class).
# Then implement the following test methods in the TestIncomeTax class:
# test_income_below_threshold() checks if for 60000 the calculated tax will be 10200
# test_income_equal_threshold() checks if for the amount 85528 ​​the calculated tax will be 14539.76
# test_income_above_threshold() checks if for the amount of 100000 the calculated tax will be 19170.8


class SimpleTaxCalculator:

    def income_tax(self, income, first_thresh=17.0, second_thresh=32.0):
        first_rate = first_thresh / 100.0
        second_rate = second_thresh / 100.0
        threshold = 85528
        if income < threshold:
            return income * first_rate
        else:
            return threshold * first_rate + (income - threshold) * second_rate

    def vat_tax(self, net_price, tax=23.0):
        tax_rate = tax / 100.0
        return net_price * tax_rate

    def capital_gains_tax(self, profit, tax=19.0):
        tax_rate = tax / 100.0
        if profit > 0:
            return profit * tax_rate
        return 0

from unittest import TestCase

class TestIncomeTax(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()
        
    def test_income_below_threshold(self):
        self.assertEqual(10200, self.calc.income_tax(60000))
    def test_income_equal_threshold(self):
        self.assertEqual(self.calc.income_tax(85528), 14539.76)
    def test_income_above_threshold(self):
        self.assertEqual(self.calc.income_tax(100000), 19170.8)