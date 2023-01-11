# Implement a solution to this problem using the object-oriented programming (OOP) paradigm. Create a class called MonteCarlo that will contain:
# the __init__() method, which will set the instance attribute named simulations
# a static method called generate_random_point(), which generates a point with coordinates in the range [-1, 1] according to a uniform distribution
# a static method called is_in_unit_circle(), which checks whether a given point falls within a circle of radius 1. The method returns True if the point is inside the circle, False otherwise
# a method called estimate(), which will simulate the number of Pi (the number of simulations is the simulations attribute) and will return the approximate value of the Pi number calculated based on the Monte Carlo method.


import random


random.seed(10)

class MonteCarlo:
    def __init__(self, simulation):
        self.simulation = simulation

    @staticmethod
    def generate_random_point():
        return random.uniform(-1, 1), random.uniform(-1, 1)

    @staticmethod
    def is_in_unit_circle(point):
        return point[0] ** 2 + point[1] ** 2 <= 1

    def estimate(self):
        points_in_circle = 0
    
        for _ in range(self.simulation):
            point = self.generate_random_point()
    
            if self.is_in_unit_circle(point):
                points_in_circle += 1
    
        result = 4 * points_in_circle / self.simulation
        return result
        

        
 

 

 
 
