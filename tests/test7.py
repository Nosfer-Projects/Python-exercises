# Using the unittest framework, a TestJoinMethod class was created that inherits from the unittest.TestCase class and implements the following three tests:
# test_join_with_space()
# test that checks if the code ' '.join(['Python', '3.8']) returns a text
# 'Python 3.8'
# test_join_with_comma()
# test that checks if the code ','.join(['open', 'high', 'low', 'close']) returns the text 'open,high,low,close'
# test_join_with_new_line_char()
# test that checks if the code '\n'.join(['open', 'high', 'low', 'close']) returns the text 'open\nhigh\nlow\nclose'
# First, run all the tests (check the solution by clicking the 'Check solution' button). Pay attention to the result. One of the tests was written incorrectly. Try to correct it and run the tests again. The solution will be passed when the error is corrected.
import sys
path= r'\\Python-exercises'
sys.path.append(path)
import unittest


class TestJoinMethod(unittest.TestCase):

    def test_join_with_space(self):
        self.assertEqual(' '.join(['Python', '3.8']), 'Python 3.8')

    def test_join_with_comma(self):
        actual = ','.join(['open', 'high', 'low', 'close'])
        expected = 'open,high,low,close'
        self.assertEqual(actual, expected)

    def test_join_with_new_line_char(self):
        actual = '\n'.join(['open', 'high', 'low', 'close'])
        expected = 'open\nhigh\nlow\nclose'
        self.assertEqual(actual, expected)