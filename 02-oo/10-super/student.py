from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def perimeter(self):
        ...
        
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
            
    @property
    def length(self):
        return self.__length
    
    @property 
    def width(self):
        return self.__width
    
    @property
    def area(self):
        return (self.__width * self.__length)
    
    @property
    def perimeter(self):
        return 2 * (self.__width + self.__length)
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
    @property
    def side(self):
        return self.__length
    
    @property
    def area(self):
        return self.side * self.side
    
    @property
    def perimeter(self):
        return 4 * self.side
    
class Ellipse:
    def __init__(self, major_radius, minor_radius):
        self.__major_radius = major_radius
        self.__minor_radius = minor_radius
        
    @property
    def major_radius(self):
        return self.__major_radius
    
    @property
    def minor_radius(self):
        return self.__minor_radius
    
    @property
    def area(self):
        return pi * self.__minor_radius * self.__major_radius
    
    @property
    def perimeter(self):
        raise NotImplementedError("There's no nice formula for this apparantly")
        
class Circle:
    def __init__(self, radius):
        self.__radius = radius
        
    @property
    def radius(self):
        return self.__radius