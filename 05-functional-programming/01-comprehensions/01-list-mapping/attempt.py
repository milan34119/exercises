# * `titles(movies)` returns the movie titles.
# * `titles_and_years(movies)` returns the movie titles and their year, grouped in pairs: `[(title1, year1), (title2, year2), ...]`.
# * `titles_and_actor_counts(movies)` returns the movie titles paired up with the number of actors.
# * `reverse_words(sentence)` must reverse each word in the given string `sentence`.
#   Words are separated by one space.

def titles(movies):
    return [movie.title for movie in movies]

def titles_and_years(movies):
    return [(movie.title, movie.years) for movie in movies]

def titles_and_actor_counts(movies):
    return [(movie.title, len(movie.actors)) for movie in movies]

def reverse_words(sentence):
    words = sentence.split(' ')
    return [word[::-1] for word in words]