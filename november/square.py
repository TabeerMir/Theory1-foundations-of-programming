class Square:
    def __init__(self,length):
        self.length = length
    
    def area(self):
        return self.length**2
        

S1 = Square(5)  
print(S1.length)
print (S1.area())