# Using the unittest framework, create two classes named: TestStartswithMethod and TestEndswithMethod inheriting from the unittest.TestCase class.
# The TestStartswithMethod class implements two test methods:
# test_startswith_one_letter()
# a test that will check if the code 'unittest'.startswith('u') returns a boolean True
# a test that will check if the 'unittest'.startswith('U') code will return the False value
# test_startswith_four_letters()
# a test that will check if the code 'http://www.e-smartdata.org/'.startswith('http') returns a boolean value True
# a test that will check if the code 'www.e-smartdata.org/'.startswith('http') returns a boolean value False
# The TestEndswithMethod class implements one test method:
# test_endswith_three_letter()
# a test that will check if the 'e-smartdata.org'.endswith('org') code returns a True value
# a test that will check if the 'e-smartdata.org'.endswith('com') code will return the False value
# All you need to do is define the classes and the appropriate test methods. During the verification of the solution, the tests are run and in the event of any errors, the test report will be printed to the console.

import unittest
import sys
path= r'\\Python-exercises'
sys.path.append(path)
 
class TestStartswithMethod(unittest.TestCase):
 
    def test_startswith_one_letter(self):
        self.assertTrue('unittest'.startswith('u'))
        self.assertFalse('unittest'.startswith('U'))
 
    def test_startswith_four_letters(self):
        self.assertTrue('http://www.e-smartdata.org/'.startswith('http'))
        self.assertFalse('www.e-smartdata.org/'.startswith('http'))
 
 
class TestEndswithMethod(unittest.TestCase):
 
    def test_endswith_three_letter(self):
        self.assertTrue('e-smartdata.org'.endswith('org'))
        self.assertFalse('e-smartdata.org'.endswith('com'))