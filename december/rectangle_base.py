#class for a rectangle
class Rectangle:
    def __init__(self,xcoord=0,ycoord=0, width=1, length=1):
        if width <=0 or length<=0:
            raise ValueError('invalid inputs (w and l must be +)')
        self.x = xcoord
        self.y = ycoord
        self._w = width
        self._l = length

    def area(self):
        return self._w*self._l
    
    #getters
    @property
    def width(self):
        return self._w
    
    @property
    def length(self):
        return self._l
    
    #setters
    @width.setter
    def width(self, w):
        if w<=0:
            raise ValueError('invalid input(width must be +)')
        self._w = w
        
    @length.setter
    def length (self, l):
        if l <=0:
            raise ValueError('invalid input(length must be +)')
        self._l = l

r1 = Rectangle()
r2 = Rectangle (1,1,2,3)
r2.width=3
r2.length =5
print(f"\n\n R1: ({r1.x}, {r1.y}, {r1.width}, {r1.length}), area ={r1.area()}")
print(f"R2:({r2.x}, {r2.y}, {r2.width}, {r2.length}), area = {r2.area()}\n\n")

#getters and setters for x and y arent doing any checking and these should be public however w and l can be modified so must be protected
