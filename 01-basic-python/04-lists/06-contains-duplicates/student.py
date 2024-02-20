# Write your code here
def contains_duplicates(xs):
    found = []
    for i in xs:
        if i in found:
            return True
        else:
            found.append(i)
    return False