def cycle(xs):
    values = list(xs)
    while True:
        for x in values:
            yield x

# def cycle(xs):
#     values = list(xs)
#     while True:
#         yield from values
#WERKEN ALLEBEI, list(xs) voor het geval dat xs een iterator is