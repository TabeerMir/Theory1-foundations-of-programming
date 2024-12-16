from math import sqrt
class Triangle:
    x1 = 0
    x2 = 0
    x3 = 0 
    y1 = 0
    y2 = 0 
    y3 = 0 
    vertices = []
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._x3 = x3
        self._y3 = y3
        vertices = [(x1,y1),(x2,y2),(x3,y3)]

    def getArea(self):
        side1 = self._y2-self._y3
        side2 = self._y3-self._y1
        side3 =self._y1-self._y2
        return (1/2*(self._x1*side1+self._x2*side2+self._x3*side3))
    
    def getPerimeter(self):
        l1 = sqrt(((self._x2 - self._x1)**2) + ((self._y2 - self._y1)**2))
        l2 = sqrt(((self._x3 - self._x2)**2) + ((self._y3 - self._y2)**2))
        l3 = sqrt(((self._x3 - self._x1)**2) + ((self._y3 - self._y1)**2))
        perimeter = l1 + l2 +l3
        return perimeter
    
    def getInscribedCircle(self):
        l1 = sqrt(((self._x2 - self._x1)**2) + ((self._y2 - self._y1)**2))
        l2 = sqrt(((self._x3 - self._x2)**2) + ((self._y3 - self._y2)**2))
        l3 = sqrt(((self._x3 - self._x1)**2) + ((self._y3 - self._y1)**2))
        centreX = (l1*self._x1 + l2*self._x2 +l3*self._x3)/l1+l2+l3
        centreY = (l1*self._y1 + l2*self._y2 +l3*self._y3)/l1+l2+l3
        centre = (centreX,centreY)
        return centre
        midpoint = ()
    
    
T1 = Triangle(2, 4, 3, -6, 7, 8)
print(T1.getArea())
print (T1.getPerimeter())
print (T1.getInscribedCircle())