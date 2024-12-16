#taking two integers as parameters and returning a binary string where a character 1 is used if the digits at the same index are the same, a 0 otherwise.
number_a = int(input('enter first number'))
number_b = int(input('enter second number'))

#if one is longer than the other, create a list and append '' for each value

def pairwise_digits(number_a, number_b):
    number_b = str(number_b)
    number_a = str(number_a)
    for digit in range (len(number_a)):   
        if number_a[digit]==number_b[digit]:
            print('1', end="")
        else:
            print ('0',end ="")

pairwise_digits(number_a, number_b) 