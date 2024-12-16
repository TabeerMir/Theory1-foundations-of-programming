# dictionaries warm up exercise
months = {'january':1, 'february':2, 'march':3,'april':4 , 'may':5, 'june':6, 'july':7, 'august':8, 'september':9, 'october':10, 'november':11, 'december':12}
print(months['january'])

roman_numerals  = {'I': 1, 'V': 5,'X': 10, 'L': 50, 'C': 100,'D': 500,'M': 1000}
elements = {'hydrogen':'H', 'helium':'He', 'lithium':'Li', 'beryllium':'Be', 'boron':'B', 'carbon':'C', 'nitrogen':'N'}


roman = {}
roman[100000]='T'
roman[1000]='M'
roman[500]='D'
roman[100]='K' 
roman[50]='L'
roman[10]='X'
roman[5]='V' 
roman[1]='I'
print(roman)

#change K to C
roman[100]='C'

#delete 100000:T pairing
del roman[100000]
print(roman)