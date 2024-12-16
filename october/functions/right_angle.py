#printing a right angle composed of 1s and 0s
rows = int(input('how many rows'))
def binary_right_angle():
    for row in range(0, rows):    
        for col in range(0, row + 1):  
            if (((row + col) % 2) == 0) : 
                print("0", end = "") 
            else: 
                print("1", end = "") 
            print("\t", end = "") 
        print("") 


binary_right_angle()

 