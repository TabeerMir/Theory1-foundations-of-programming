def len_string(string):
    if string:
        return 1 + len_string(string[1:])
    else:
        return 0
    

print(len_string('racecar')) 
