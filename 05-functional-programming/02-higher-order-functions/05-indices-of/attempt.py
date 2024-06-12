# Write a function `indices_of(xs, condition)` that returns the indices of all the elements for which `condition` returns a truthy value.
def indices_of(xs, condition):
    result = []
    i = 0
    while i < len(xs) and condition(i):
        i += 1
        result.append(i)
    return result
        