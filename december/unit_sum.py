def digital_root_sum (n):
    def digital_sum(num):
        if num <10:
            return num
        else:
            num = str(num)
            return int(num[0]) + digital_sum(int(num[1:]))
    
    x= digital_sum(n)
    
    if x>9: 
        return digital_root_sum(x)
    else:
        return x
    
print(digital_root_sum(1028))