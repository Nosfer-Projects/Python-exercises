# The following calculate_daily_return() function is provided, which takes two arguments: open and close, which are the opening price and closing price of a financial instrument from a given trading session, respectively, and returns the percentage value of the daily rate of return.
# def calculate_daily_return(open, close):
#     return round((close / open - 1) * 100, 2)
# Complete the implementation of the TestCalculateDailyReturn class by adding three test methods:
# test_positive_return()
# using the assertEqual method, check if the calculate_daily_return(349.0, 360.0) code will return a daily rate of return of 3.15
# test_negative_return()
# using the assertEqual method, check if the calculate_daily_return(349.0, 340.0) code will return a daily rate of return -2.58
# test_zero_return()
# using the assertEqual method, check if the calculate_daily_return(349.0, 349.0) code will return a daily rate of return of 0.0
# You only need to implement test methods. During the verification of the solution, the tests are run and in the event of any errors, the test report will be printed to the console.
import sys
path= r'\\Python-exercises'
sys.path.append(path)
import unittest


def calculate_daily_return(open, close):
    return round((close / open - 1) * 100, 2)


class TestCalculateDailyReturn(unittest.TestCase):
    def test_positive_return(self):
        self.assertEqual(calculate_daily_return(349.0, 360.0), 3.15)
    def test_negative_return(self):
        self.assertEqual(calculate_daily_return(349.0, 340.0), -2.58)
    def test_zero_return(self):
        self.assertEqual(calculate_daily_return(349.0, 349.0), 0.0)
    