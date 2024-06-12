# * `directors(movies)` collects all directors in a set.
# * `common_elements(xs, ys)` should return the set of values that occur both in `xs` and `ys`.

def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs, ys):
    return {x for x in xs if x in ys}


