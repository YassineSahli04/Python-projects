'''Write a Python  class named Circle constructed by its center O and radius r. 
Define two methods, area and perimeter, which will compute the area and the perimeter of the circle,
and is Inside() method which allows you to test whether a point A(x, y) belongs to the circle C(O, r)'''
import math
from math import *
pi = math.pi 
class circle:
    def __init__(self, radius, point_x, point_y):
        #self.center = center
        self.radius = radius
        self.point_x = point_x
        self.point_y = point_y

    def area(self):
        area = (self.radius **2 )* pi
        return area
    def perimeter(self):
        perimeter = self.radius * 2 * pi
        return perimeter
    def inside(self):
        length_A = sqrt((self.point_x ** 2) + (self.point_y ** 2))
        if length_A > self.radius:
            belonging = print(f"The point A({self.point_x},{self.point_y}) don't belongs to the circle C(0, {self.radius}) ")
        else:
            belonging = print(f"The point A({self.point_x},{self.point_y}) belongs to the circle C(0, {self.radius}) ")
        return belonging

my_circle = circle(10, 1 , 1)
print("Area: " , my_circle.area())
print("Perimeter: " ,  my_circle.perimeter())
print(my_circle.inside())