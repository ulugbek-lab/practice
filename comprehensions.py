'''Comprehension
1. what is comprehension
2. set and dictionary comp
'''
print("=========what is comprehension & list comprehension =========")
# Comprehension act like spread operators

'''Comprehensions general syntax:
a) *Iterable 
b) <Expression> for items in iterable
c) <Expression> for items in iterable <condition>
'''


# List comp.
numbers = [1, 2, 3, 4, 2, 12, 1]
list_numbers = [*numbers]  # a version (same value but different ID)
print(list_numbers)

print("-------")
people = [("Ross", 33), ("steve", 65), ("mark", 23)]
list_people = [person[0]for person in people]  # b version
print(list_people)

cars = [
    ("ferrasri", 23),
    ("toyota", 87),
    ("mazda", 43),
    ("audi", 116),
    ("pagani", 33)
]
list_cars = [car[1]for car in cars if car[1] > 80]  # c version
print(list_cars)

