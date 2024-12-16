data = [[1,2,3], [2], [1, 2, 3, 4]]
output = []


def sum_lists(data):
    for row in data:
        total = 0
        for value in row:
            total = total+value
        output.append(total)
    print(output) 

sum_lists(data)