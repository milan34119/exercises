# Each function must leave its argument unmodified and return a new list.

# * `sort_by_age(people)` orders the `Person`s by increasing `age`.
# * `sort_by_decreasing_age(people)` orders the `Person`s by decreasing `age`.
# * `sort_by_name(people)` orders the `Person`s by `name`, alphabetically.
# * `sort_by_name_then_age(people)` orders the `Person`s by `name`, and in case of equal `name`s, by increasing `age`
# * `sort_by_name_then_decreasing_age(people)` orders the `Person`s by `name`, and in case of equal `name`s, by decreasing `age`

from operator import attrgetter
def sort_by_age(people):
    return sorted(people, key=lambda person: person.age)

def sort_by_age(people):
    return sorted(people, key=attrgetter('age'))

def sort_by_decreasing_age(people):
    return sorted(people, key= lambda person: -person.age)

def sort_by_name(people):
    return sorted(people, key= lambda person: person.name)

def sort_by_name_then_age(people):
    return sorted(people, key= lambda person: (person.name, person.age))

def sort_by_name_then_decreasing_age(people):
    return sorted(people, key=lambda person: (person.name, -person.age))

def sort_by_name_then_decreasing_age(people):
    return sorted(people, key=attrgetter('name, age'))
