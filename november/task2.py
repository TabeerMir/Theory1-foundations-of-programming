sentences = ['hello', 'my', 'name', 'is', 'tabi']
filename = 'task2file.txt'

def save_list2file(sentences, filename):
    for word in sentences:
        f = open(filename, 'a')
        f.write('\n')
        f.write(word)
    

save_list2file(sentences,filename)
