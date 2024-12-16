#takes two list of the same length as parameters and returning a dictionary - if keys has duplicates then an error message occurs

keys = ['one','two','three']
values = [1, 2, 3]


def map_list(keys,values):
    if len(keys) != len(values):
        return None
    
    count=len(keys)
    mapped_dico = {}
    for x in range(count):
        if keys[x] not in mapped_dico:
            mapped_dico[keys[x]] = values[x]
        else:
            print('error: duplicate key')
            return None
    print (mapped_dico)

map_list(keys,values)