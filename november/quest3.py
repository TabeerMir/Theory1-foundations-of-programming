def sum_integers(start, end):
    total = 0
    if end<start or start<0 or end<0:
        return -1
    else:
        for i in range(start,end+1):
            total = total+i
    return total

sum_integers(-2,4)