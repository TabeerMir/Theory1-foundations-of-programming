def rec_sum(numbers):
    length = len(numbers)
    if length ==0:
        return 0
    elif length ==1:
        return numbers[0]
    else: 
        return numbers[0] + rec_sum(numbers[1:])
    

print(rec_sum([1,2,3,4]))
print (rec_sum([]))
