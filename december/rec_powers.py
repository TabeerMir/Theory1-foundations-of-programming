

def is_power(a,b):
    if b == 0:
        if a == 0:  # 0 not a power of anything
            return True
        else:
            return False
    if a == 1:
        return True
    elif b == 1:
        return False
    elif a%b == 0:
        return is_power(a/b,b)
    else:
        return False
    
print(is_power(64,2))