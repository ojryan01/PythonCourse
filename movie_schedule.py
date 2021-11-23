
current_movies = { 'The Grinch' : '11:00am', 'Rudolph': '12:00pm', "Christmas Story" : '3:00pm'}

print('Movie schedule: ', current_movies )

for key in current_movies:
    print(key)

movie = input("Which movie would you like showtimes for? \n")


showtime = current_movies.get(movie)

if showtime == None:
    print("That movie isn't showing")
else:
    print(showtime)