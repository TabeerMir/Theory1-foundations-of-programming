def merge_lists (list1, list2):
    if list1 == []:
        return list2
    elif list2 == []:
        return list1
    elif list1[0] < list2[0]:
        return [list1[0]] + merge_lists(list1[1:], list2)
    else:
        return [list2[0]] + merge_lists(list1, list2[1:])
    
print(merge_lists([1,3,5,7], [2,4,6,8]))