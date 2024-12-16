class Car:
    def __init__(self,speed,colour):
        self.__speed = speed
        self.__colour = colour
    
    #setters
    def set_speed(self,value):
        self.__speed = value
    
    def set_colour(self,value):
        self.__colour = value

    #getter
    def get_speed(self):
        return self.__speed
    
    def get_colour(self):
        return self.__colour


ford = Car(200,'red')
honda = Car(250,'blue')
audi = Car(300,'black')

ford.set_speed(300)
print(ford.get_speed())
print(ford.get_colour)