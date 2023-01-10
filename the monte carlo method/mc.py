# Consider the Monte Carlo method. It is a method used for mathematical modeling of quite complex processes, in order to approximate the result using an analytical approach. An important role in this method is played by the randomization of the quantities characterizing the process.
# We will use the Monte Carlo method to approximate Pi. Consider a circle of radius 1 and centered at the origin (R^2 space). The area of ​​a circle with a circle defined in this way is exactly Pi. Let's add to this the square circumscribed about this circle with vertices at (1, 1), (1, -1), (-1, -1), (-1, 1). The side of this square is 2 and its area is 4.
# Our task is to draw points from the given square according to the uniform distribution and check whether the drawn point falls into the circle. The probability of such an event is equal to the area of ​​a circle of radius 1, which is exactly Pi.
# We choose the number of simulations arbitrarily, but basically the more simulations we carry out, the better we will get the approximation of Pi.
# Single simulation: We draw a point from a square according to a uniform distribution and check if it lies inside the given circle.
# The area of ​​a circle can be determined from the formula:
# area of ​​the circle = area of ​​the square * (number of points drawn inside the circle / number of all points drawn)
# Since we know that the area of ​​the circle thus defined is Pi, we can make the substitution:
# Pi = area of ​​the square * (number of points drawn inside the circle / number of all points drawn)
# A function called generate_random_point() has been implemented, which generates a point with coordinates in the range [-1, 1] according to a uniform distribution.
# Implement a function called is_in_unit_circle() that checks if a given point falls within a circle of radius 1. The function should return True if the point is inside the circle, False otherwise.
# Set the random seed to 20 and pseudo-randomly generate 15 points by assigning them to a list called points. Then, at each point in the list, call is_in_unit_circle() and assign flags to the variable. In response, print the contents of the flags variable.

import random
 
 
random.seed(20)
 
 
def generate_random_point():
    return random.uniform(-1, 1), random.uniform(-1, 1)
 
 
def is_in_unit_circle(point):
    return point[0] ** 2 + point[1] ** 2 <= 1
 
 
points = [generate_random_point() for _ in range(15)]
flags = [is_in_unit_circle(point) for point in points]
print(flags)

