# The following function is given to calculate the length of a circle with a given radius:
# def perimeter(radius):
#     """The function returns the length of the circle."""
#     if not (isinstance(radius, (int, float))):
#         raise TypeError('The radius must be of type int or float.')
#     if not radius > 0:
#         raise ValueError('The radius must be positive.')
#     return 2 * math.pi * radius
# Implement a TestPerimeter class that inherits from unittest.TestCase and implements four different tests. Choose your tests freely. Use several different assertion methods.

import unittest
import math


def perimeter(radius):
    """The function returns the length of the circle."""

    if not (isinstance(radius, (int, float))):
        raise TypeError('The radius must be of type int or float.')

    if not radius > 0:
        raise ValueError('The radius must be positive.')

    return 2 * math.pi * radius

class TestPerimeter(unittest.TestCase):
    def test_type_int_float_wrong(self):
        self.assertRaises(TypeError, perimeter, "5")
    def test_type_int_float_correct(self):
        self.assertTrue(perimeter, 5)
    def test_value_error(self):
        self.assertRaises(ValueError, perimeter, 0)
    def test_correct_return(self):
        self.assertAlmostEqual(6.283185,perimeter(1), 5)