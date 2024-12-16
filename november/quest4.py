import random

def scramble(word):
    if len(word)<6:
        word = word
        return(word)
    else: 
        new_word = word[:2]
        middle =[]
        for char in word[2:(len(word)-2)]:
            middle.append(char)
        random.shuffle(middle)
        for i in middle:
            new_word = new_word + str(i)
        new_word = new_word + word[(len(word)-2):]
        return(new_word)

        

        

print(scramble('qwertyuiop'))
