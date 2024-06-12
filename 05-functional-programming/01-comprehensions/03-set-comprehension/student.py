def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs, xy):
    return {element for element in xs if element in xy}