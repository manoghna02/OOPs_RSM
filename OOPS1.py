#1. Rectangle Class
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    
smallRectangle=Rectangle(6,3)
largeRectangle=Rectangle(12,6)

smallArea=smallRectangle.area()
smallPerimeter=smallRectangle.perimeter()

largeArea=largeRectangle.area()
largePerimeter=largeRectangle.perimeter()

print("Small Rectangle:")
print("Area:", smallArea)
print("Perimeter:", smallPerimeter)

print("Large Rectangle:")
print("Area:", largeArea)
print("Perimeter:", largePerimeter)


