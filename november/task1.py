#define whats being written
a_word = 'hello'

#use with statement to open file for writing, specify file name and w mode for writing, encoding
f = open('exo1.txt', 'a')
f.write(a_word)