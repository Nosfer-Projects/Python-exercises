# Using the unittest framework, create a TestSplitMethod class that inherits from the unittest.TestCase class and implements the following three tests:
# test_split_by_default()
# test that will check if 'Python Testing'.split() returns a list
# ['Python', 'Testing']
# test_split_by_comma()
# a test that will check if the code 'open,high,low,close'.split(',') returns a list
# ['open', 'high', 'low', 'close']
# test_split_by_hash()
# a test that will check if the code 'summer#time#vibes'.split('#') will return a list
# ['summer', 'time', 'vibes']
# All you need to do is define the class and the appropriate tests. During the verification of the solution, the tests are run and in the event of any errors, the test report will be printed to the console
import sys
sys.path.append(r'\Python-exercises')
print(sys.path)
from unittest import TestCase

class TestSplitMethod(TestCase):

    def test_split_by_default(self):
        self.assertEqual('Python Testing'.split(), ['Python', 'Testing'] )

    def test_split_by_comma(self):
        self.assertEqual('open,high,low,close'.split(','), ['open', 'high', 'low', 'close'] )

    def test_split_by_hash(self):
        self.assertEqual('summer#time#vibes'.split('#'), ['summer', 'time', 'vibes'] )