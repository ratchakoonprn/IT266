#Create a movie dictionary
movie = {
    'title' : 'mulan',
    'year' : 2020,
    'runtime': 116,
    'languages' : ['English', 'Chinese', 'Thai'], #A list in the movie dictionary
    'genre' : ['Action', 'Adventure', 'Drama'] #A list in the movie dictionary
}
print('The genre of Mulan movies:')
for g in movie['genre']:
    print('\t',g)
