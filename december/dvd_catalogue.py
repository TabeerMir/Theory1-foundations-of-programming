class DVDCatalogue:
    def __init__(self, movie_list=None):
        if movie_list is None:
            self._movies = []
        else:
            self._movies=movie_list.copy()

    def add_movie(self,movie):
        self._movies.append(movie)

    def __getitem__(self,index):
        return self._movies[index]
    
    def __setitem__(self,index,value):
        self._movies[index] = value
    
    def __delitem__(self,index):
        del self._movies[index]

    def __len__(self):
        return len(self._movies)
    
    def __repr__(self):
        return f"DVDCatalogue({self._movies})"
    
    def __iter__(self):
        self.current_index = 0
        return self
    
    def __next__(self):
        if self.current_index < len(self._movies):
            current_movie = self._movies[self.current_index]
            self.current_index +=1
            return current_movie
        else: 
            raise StopIteration
    


movies = ['Monsters Inc.','Cars','Wicked',]
my_dvds = DVDCatalogue(movies)

print('\n------------iterable list-------------')
for movie in my_dvds:
    print(movie)

print('\n-------------initial list---------------')
for index in range(len(my_dvds)):
    print(index + 1, ':', my_dvds[index])

my_dvds[0] = 'Monsters University'
del my_dvds[2]

print('\n-------------updated list---------------')
for index in range(len(my_dvds)):
    print(index + 1, ':', my_dvds[index])

