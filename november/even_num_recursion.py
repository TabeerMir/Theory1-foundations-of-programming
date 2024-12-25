def even_nums(num):
    print(num)
    if num%2 !=2:
        print('pls enter an even number')
    elif num == 2:
        return num
    else:
        return even_nums(num-2)

even_nums(8)
