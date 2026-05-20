'''Comprehension
1. what is comprehension
2. set and dictionary comp
'''
print("=========what is comprehension & list comprehension =========")
# Comprehension act like SPREAD operators

'''Comprehensions general syntax:
a) *Iterable 
b) <Expression> for items in iterable
c) <Expression> for items in iterable <condition>
'''


# List comp.
numbers = [1, 2, 3, 4, 2, 12, 1]
list_numbers = [*numbers]  # a version (same value but different ID) spread operator
print(list_numbers)

print("-------")
people = [("Ross", 33), ("steve", 60), ("mark", 23), ("steve", 60)]
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

print("========= set & dictionary comprehension  =========")
numbs = [1, 2, 8, 4, 2, 12, 1]
set_numbs = {*numbs}
print(set_numbs)

dict_people = {person[0]: person[1] for person in people}  # b version
print(dict_people)
dict_people = {person[0]: person[1]
               for person in people if person[1] > 30}  # c version
print(dict_people)
