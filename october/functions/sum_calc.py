#calculate and return the sum of the digits of an integer input
number = input('please enter a number')

def sum_digits(number):
    total = 0
    for i in number:
        i = int(i)
        total = total+i
    print (total)

sum_digits(number)
 