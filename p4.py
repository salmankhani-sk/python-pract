class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    
# Test the Rectangle class
obj1 = Rectangle(3, 2,)

print("Area:", obj1.area())

print("Perimeter:", obj1.perimeter())
