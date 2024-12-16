#reversing the mapping between keys and values
dico = {'one':1,'two':2,'three':3, 'four':4}
reversed_dico = {}

def reversed_dictionary (dico):
    for key, value in dico.items():
        if value in reversed_dico:
            print('error')
            return None
        reversed_dico[value] = key
    print (reversed_dico)


        
reversed_dictionary(dico)
