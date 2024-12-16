def ispalindrome(word):
    length = len(word)
    print(length)
    if length <=1:
        return True
    elif length ==2:
        if word[0] ==word[1]:
            return True
        else:
            return False
    elif length >2 and word[0] == word[-1]:
        newword = word[1:-1]
        return ispalindrome(newword)
    else:  
        return False
    


print(ispalindrome('racecar'))