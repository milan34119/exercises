
# * `movies_from_year(movies, year)` returns the titles of movies from the given `year`.
# * `movies_with_actor(movies, actor)` returns the titles of movies that have `actor` in it.
# * `divisors(n)` returns the divisors of `n` in increasing order. For example, `divisors(12)` should return `[1, 2, 3, 4, 6, 12]`.

def movies_from_year(movies, year):
    return [movie.title for movie in movies if movie.year == year]

def movies_with_actor(movies, actor):
    return [movie.title for movie in movies if actor in movie.actors]

def divisors(n):
    return [k for k in range(1, n+1) if n%k == 0]