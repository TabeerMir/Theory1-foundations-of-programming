fnumber = open('fnumber.txt','r')

def sum_from_file(fnumber):
    sum_of_line=0
    for line in fnumber:
        sum_of_line = sum_of_line + sum_numbers(line)
    print(sum_of_line)


def sum_numbers(num_string):
    nums = num_string.split(" ")
    sum=0
    for num in nums:
        sum = sum + int(num)
    return(sum)




sum_from_file(fnumber)

fnumber.close()








