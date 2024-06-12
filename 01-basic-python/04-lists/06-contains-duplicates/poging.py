def contains_duplicates(xs):
    result = []
    for x in xs:
        if x not in result:
            result.append(x)
        else:
            return True
    return False