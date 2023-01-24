# The SimpleTaxCalculator class is implemented in tax.py. Add a TestVatTax class that inherits from unittest.TestCase to the solution file called exercise.py. Add the setUpClass() class method to create an instance of the SimpleTaxCalculator class and assign it to the attribute named calc of the TestVatTax class (assignment at the level of the TestVatTax test class).
# Then implement the following test methods in the TestVatTax class:
# test_vat_tax_with_default() checks if for the amount of 100 the calculated tax will be 23.0
# test_vat_tax_with_twenty_tax_rate() checks if for an amount of 100 and a tax rate of 20% the calculated tax will be 20.0
# All you need to do is implement the class and the appropriate test methods. During the verification of the solution, the tests are run and in the event of any errors, the test report will be printed to the console.

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
import unittest


class TestIncomeTax(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()

    def test_income_below_threshold(self):
        self.assertEqual(self.calc.income_tax(60000), 10200)

    def test_income_equal_threshold(self):
        self.assertEqual(self.calc.income_tax(85528), 14539.76)

    def test_income_above_threshold(self):
        self.assertEqual(self.calc.income_tax(100000), 19170.8)
class TestVatTax(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()
        
    def test_vat_tax_with_default(self):
        self.assertEqual(23.0, self.calc.vat_tax(100))

    def test_vat_tax_with_twenty_tax_rate(self):
        self.assertEqual(20.0, self.calc.vat_tax(100, 20))