def add_triathlon_data(entry, records):
    entry_list = entry.split(',')
    entry_length= len(entry_list)
    type = True
    key = entry_list[0]
    data = entry_list[1:]

    for i in data:
        try:
             x = int(x)
        except:
            type = False

    if entry_length < 4 or key in records or type == False:
        return False
    else:
        data_dict = {'run':entry_list[0],'swim':entry_list[1],'bike':entry_list[2]}
        records[key]=data_dict
        return True

records={}
add_triathlon_data("Javier Gomez,1756,1020,3556",records)