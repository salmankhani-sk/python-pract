class Rectangle():
    def __init__(self,width, height):
        self.width = width
        self.height = height 
    def area(self):
        return self.width * self.height
    def parameters(self):
        return 2 * (self.width + self.height)
try :
    w : int = int(input("Enter the width of a Rectangle :"))
    h : int = int(input("Enter the height of a Rectangle :"))
    obj1 = Rectangle(width=w, height=h)
    print("The Area of the Rectangle is :", obj1.area())
    print("The Perimeter of the Rectangle is :", obj1.parameters())
except ValueError:
    print("Invalid Input Please enter Integers value only")