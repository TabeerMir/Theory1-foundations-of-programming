

class RomanNumeral:
    roman_map = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
    
    def __init__(self,value):
        self.value = value 

    def to_roman(self):
        result = ''
        num = self.value
        for val in sorted(self.roman_map.keys(), reverse=True):
            while num >= val:
                result += self.roman_map[val]
                num -= val
        return result
    
    
    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.value == other.value
        return False
    
    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.value < other.value
        raise TypeError ('comparison with incompatible type')
    
    #could use @total_ordering instead of the section below
    
    def __le__(self,other):
        return self == other or self<other
    
    def __ge__(self,other):
        return self == other or not self < other
    
    def __gt__(self, other):
        return self != other and not self<other
    
    def __ne__(self,other):
        return not self == other
    

    def __repr__(self):
        return f"RomanNumeral({self.value})"
    
Num1 = RomanNumeral(14)
Num2 = RomanNumeral(8)
print(Num1.to_roman())
print(Num2.to_roman())
print(Num1==Num2)
print(Num1<Num2)
print(Num1<=Num2)
print(Num1>Num2)
print(Num1>=Num2)

