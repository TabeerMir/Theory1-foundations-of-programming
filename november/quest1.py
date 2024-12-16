def create_triangle(n):
    lines=''
    if n == 0:
        return ''
    elif n<0:
        return None
    else:
        for i in range (n) :
            lines = lines+ ('x'*(i+1))+('-'*(n-(i+1)))+ '\n'
        return lines

        
        

print(create_triangle(10))
