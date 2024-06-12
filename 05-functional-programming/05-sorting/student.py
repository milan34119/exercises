from operator import attrgetter

# def sort_by_age(people):
#     return sorted(people, key= lambda people : people.age)

# def sort_by_decreasing_age(people):
#     return sorted(people, key= lambda people : -people.age)

# def sort_by_name(people):
#     return sorted(people, key= lambda people : people.name)

# def sort_by_name_then_age(people):
#     return sorted(people, key= lambda people : (people.name, people.age))

# def sort_by_name_then_decreasing_age(people):
#     return sorted(people, key= lambda people : (people.name, -people.age))

#Andere manieren:
def sort_by_age(people):
    return sorted(people, key= attrgetter('age'))

def sort_by_decreasing_age(people):
    return sorted(people, key= attrgetter('age'), reverse= True)

def sort_by_name(people):
    return sorted(people, key= attrgetter('name'))

def sort_by_name_then_age(people):
    return sorted(people, key= attrgetter('name', 'age'))

def sort_by_name_then_decreasing_age(people):
    return sorted(people, key= lambda people : (people.name, -people.age))