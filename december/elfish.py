def iselfish(word, elf):
    if elf == []:
        return True
    elif word == '':
        return False
    elif elf[0] in word:
        word = word.replace(elf[0],'')
        return iselfish(word,elf[1:])
    else: 
        return False



print(iselfish('friendly',['e', 'l', 'f']))
print(iselfish('pencil',['e', 'l', 'f']))
print(iselfish('smile',['e', 'l', 'f']))
print(iselfish('elf',['e', 'l', 'f']))


def something_ish(word, pattern):
    if pattern == []:
        return True
    elif word == '':
        return False
    elif pattern[0] in word:
        word = word.replace(pattern[0],'')
        return something_ish(word,pattern[1:])
    else: 
        return False

print(something_ish('stinky',['t', 'i', 'k']))