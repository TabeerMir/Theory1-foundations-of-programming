class Person:
    def __init__(self,name,height,weight,hair,eyes,shoe):
        self.my_name = name
        self.my_height = height
        self.my_weight = weight
        self.my_hair = hair 
        self.my_eyes = eyes
        self.my_shoes = shoe

P1 = Person('hexi',10,12,'brown','green',4)
print(P1.my_name)