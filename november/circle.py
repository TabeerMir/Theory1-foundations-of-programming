class Circle:
    def __init__(self,centre,radius):
        self._centre = centre
        self._radius = radius

    def getArea(self):
        return ((self._radius**2)*3.14)
    
    def getPerimeter(self):
        return (2*3.14*self._radius)
    
C1=Circle((2,3),5)
print(C1.getArea())
print(C1.getPerimeter())