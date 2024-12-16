class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def perimiter(self):
        return (2*self.length)+(2*self.width)
     
R1 = Rectangle(2,4)
print(R1.area())
print(R1.perimiter())