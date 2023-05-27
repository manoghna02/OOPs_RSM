#5. Shape Class Hierarchy
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Circle(shape):
    def __init__(self, radius):
        self.radius=radius
    def calculate_area(self):
        return 3.14*(self.radius**2)
    
class Rectangle(shape):  
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        return self.length*self.width

class Triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def calculate_area(self):
        return 1/2*self.base*self.height
    
myCircle=Circle(2)
print("Area of circle is", myCircle.calculate_area())
myRectangle=Rectangle(6,6)
print("Area of rectangle is:", myRectangle.calculate_area())
myTriangle=Triangle(2,3)
print("Area of triangle is:", myTriangle.calculate_area())      
    