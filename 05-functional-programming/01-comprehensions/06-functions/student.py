def movie_count(movies, director):
    return len([
        movie for movie in movies if director == movie.director
    ])
    
def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor == movie.actor])

def has_director_made_genre(movies, director, genre):
    return any(genre in movie.genres and movie.director == director for movie in movies)

def is_prime(n):
    return all(n % k != 0 for k in range(2, n)) and n >= 2

def is_increasing(ns):
    xs = enumerate(ns)
    for k in range(0, ns+1):
        if k < xs[i]:
            