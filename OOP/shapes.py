#!/usr/bin/env python3
from abc import ABC
import math

"""
Shape Hierarchy:
Define a base class Shape and create subclasses such as Circle, Rectangle, and Triangle. 
Implement methods to calculate the area and perimeter for each shape. 
Explore polymorphism by creating a list of different shapes and calculating their total area.
"""


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        """Area abstract"""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimeter abstract"""
        pass


class Circle(Shape):
    def __init__(radius: float):
        self.radius = radius

    def area(radius: float):
        return math.pi * math.pow(radius, 2)
    
    def perimeter(radius: float):
        return 2 * math.pi * radius


class Rectangle(Shape):
    def __init__(width: float, length: float):
        self.width = width
        self.length = length

    def area(width: float, lenght: float):
        return width * lenght
    
    def perimeter(radius: float):
        return 2 * (width + lenght)


class Triangle(Shape):
    def __init__(a: float, b: float, c: float):
        self.width = width
        self.length = length

    def area(height: float, base: float):
        return (height * base) / 2
    
    def perimeter(a: float, b: float, c: float):
        return a + b + c
    
# class based plymorphism means we are implementing methods with same name
# allowing us to loop over different shapes calling a single method `area`
shapes = [
    Circle(5),
    Rectangle(10, 20),
    Triangle(1, 2, 3)
]

total_area = 0
for s in shapes:
    total_area += s.area()

print(f"Total Area: {total_area}")
