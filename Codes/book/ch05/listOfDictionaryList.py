#Nesting - A list of dictionaries
movie_0 = {'title':'mulan','year':2020,'runtime':116}
movie_1 = {'title':'black box','genre':'mystery and thriller','runtime':100}
movie_2 = {'title':'godzilla vs. kong','runtime':100,'imdb':6.5}
#create movies list
movies = [movie_0,movie_1,movie_2]
#print movie details
print('**** All movies  list ****')
for m in movies:
    print(m)
#print the first two movies
print('---- The first 2 moveis ----')
print(movies[:2])
