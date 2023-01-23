# Using the unittest framework, create a TestUpper class that inherits from the unittest.TestCase class and implements the following two tests:
# test_upper()
# a test that will check if the code 'summer'.upper() returns the text 'SUMMER'
# test_is_upper()
# a test that will check if the code 'SUMMER'.isupper() returns a boolean True
# a test that will check if the code 'summer'.isupper() returns a boolean value False
# All you need to do is define the class and the appropriate tests. During the verification of the solution, the tests are run and in the event of any errors, the test report will be printed to the console.

import unittest
import sys
path= r'\\Python-exercises'
sys.path.append(path)
 
 
class TestUpper(unittest.TestCase):
 
    def test_upper(self):
        self.assertEqual('summer'.upper(), 'SUMMER')
 
    def test_is_upper(self):
        self.assertTrue('SUMMER'.isupper())
        self.assertFalse('summer'.isupper())
