#taking 2 dictionaries and combining them to form a new one - if a common key arises in the two dictionaries this gets stored in a list

dico1 ={'one':1, 'two':2, 'three':3}
dico2 = {'three':'three','four':4, 'five':5}

def concat_dico(dico1,dico2):
    new_dico ={}
    new_dico.update(dico1)
    new_dico.update(dico2)
    
    for x in dico1:
        if x in dico2:
            listed_values =[]
            listed_values.append(dico1[x])
            listed_values.append(dico2[x])
            new_dico[x] = listed_values
    
    print (new_dico)

concat_dico(dico1,dico2)