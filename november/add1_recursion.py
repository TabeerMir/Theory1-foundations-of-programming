def add_one(num):
    if num>=9:
        return num+1
    else:
        total = num +1
        print(total)
        return add_one(total)
    
new_total = add_one(0)
print (new_total)