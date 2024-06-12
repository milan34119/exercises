def indices_of(xs, condition):
    result = []
    for i in range(len(xs)):
        if condition(xs[i]):
            result.append(i)
    return result
    