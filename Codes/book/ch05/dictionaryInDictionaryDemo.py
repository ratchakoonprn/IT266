#Create a movie dictionary
movies = {
	'Mulan' :{
		'wins' : 4,
		'nominations' : 44
	},
    'Black Box' : {
		'wins' : 6,
		'nominations' : 1
	}
}
#print movie and award
for name, award in movies.items():
	print('Movie : ',name)
	print('\tWins: ',award['wins'])
	print('\tNomiatona: ',award['nominations'])
