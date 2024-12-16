#taking a dictionary as parameter and printing the content of the dictionary, one paired element per line
dico = {'un':1, 'deux':2, 'trois':3}
def display_dico(dico):
    for number in dico:
        translation=dico[number]
        print (number, '--->', translation) 
display_dico(dico)

