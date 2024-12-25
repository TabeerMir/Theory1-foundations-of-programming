def flatten (mlist):
    if mlist == []:
        return mlist
    elif isinstance(mlist, list):
        return flatten(mlist[0]) + flatten(mlist[1:])
    elif isinstance(mlist, (float, int)):
        return [mlist]
    else: 
        raise TypeError("invalid type in the list")
    

print(flatten([1,[2,3],4]))