# Using the unittest framework, create a TestLower class that inherits from the unittest.TestCase class and implements the following two tests:
# test_lower()
# test to see if 'Joe.Smith@mail.com'.lower() returns 'joe.smith@mail.com'
# test_is_lower()
# a test that will check if the code 'joe.smith@mail.com'.islower() returns a boolean value True
# a test that will check if the code 'Joe.Smith@mail.com'.islower() returns a boolean value False
# All you need to do is define the class and the appropriate tests. During the verification of the solution, the tests are run and in the event of any errors, the test report will be printed to the console.

import unittest
import sys
path= r'\\Python-exercises'
sys.path.append(path)

class TestLower(unittest.TestCase):
    def test_lower(self):
        self.assertEqual("joe.smith@mail.com", "Joe.Smith@mail.com".lower())

    def test_is_lower(self):
        self.assertTrue('joe.smith@mail.com'.islower())
        self.assertFalse('Joe.Smith@mail.com'.islower())

