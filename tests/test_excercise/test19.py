# The SimpleTaxCalculator class is implemented in tax.py. Add a TestCapitalGainsTax class that inherits from unittest.TestCase to the solution file called exercise.py. Add a setUpClass() class method to create an instance of the SimpleTaxCalculator class and assign it to the attribute named calc of the TestCapitalGainsTax class (assignment at the TestCapitalGainsTax test class level).
# Then implement the following test methods in the TestCapitalGainsTax class:
# test_positive_profit() checks if the calculated tax will be 190.0 for the amount of 1000
# test_zero_profit() checks if the calculated tax will be 0.0 for zero profit
# test_negative_profit() checks if for a negative profit -1000 the calculated tax will be 0.0

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
        self.assertEqual(self.calc.vat_tax(100), 23.0)
 
    def test_vat_tax_with_twenty_tax_rate(self):
        self.assertEqual(self.calc.vat_tax(100, 20.0), 20.0)
 
 
class TestCapitalGainsTax(unittest.TestCase):
 
    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()
 
    def test_positive_profit(self):
        self.assertEqual(self.calc.capital_gains_tax(1000), 190.0)
 
    def test_zero_profit(self):
        self.assertEqual(self.calc.capital_gains_tax(0), 0.0)
 
    def test_negative_profit(self):
        self.assertEqual(self.calc.capital_gains_tax(-1000), 0.0)