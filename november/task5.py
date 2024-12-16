input_file = open('task5_input.txt', 'r')
output_file = open('output_file.txt', 'w')

def to_upper_case(input_file, output_file):
    for word in input_file:
        output_file.write(word.upper())

to_upper_case(input_file,output_file)
