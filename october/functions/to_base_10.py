#converting from binary to denary
def to_base10(num):
    length = len(num)
    binary_num = list(num)
    denary = 0
    for x in range (length):
        element = int(binary_num[x])
        if element == 1:
            indices = length - (x+1)
            denary = denary +pow(2,indices)
    print(denary)

num = input('enter binary')
to_base10(num)
