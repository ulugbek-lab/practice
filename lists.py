'''List 
1, workibng with list 
2. list methods
3. lambda function
4. enumerate, map, filter
'''

print("========working with list============")

# literal
person = {"name": "chris", "age": 22}
people = ("andrew", "john", "mike")

group = ["mit", "flexy", "devex"]
for member in group:
    print(member)


# constructure
letters = list("hello world")
print(letters, len(letters))


print("---------")
fruits = ["apple", "orange", "cheerry", "kiwi"]
a = fruits[0]
b = fruits[0:2]  # [0, 2) ['apple', 'orange']
c = fruits[::3]  # ['apple', 'kiwi']
d = fruits[::-1]  # ['kiwi', 'cheerry', 'orange', 'apple']


print(a)
print(b)
print(c)
print(d)


print("========list methods============")
# Methods > append() insert() pop() remove() clear() sort()   index()  all mutable except index

letters = ["a", "d", "b"]

letters.append("c")  # add last
print(letters)  # 'a', 'd', 'b', 'c']

letters.insert(0, "z")
print(letters)  # ['z', 'a', 'd', 'b', 'c']

size = len(letters) - 1
result = letters.pop(size)  # pop last
# the result: c and letters ['z', 'a', 'd', 'b']
print(f"the result: {result} and letters {letters}")


result1 = letters.pop(0)  # pop front
print(result1)  # z


print("---------------")
animals = ["dog", "cat", "capybara", "wolf", "tiger"]
print(animals)
animals.remove("tiger")  # remove
print(animals)

del animals[2:4]
print(animals)

exist = animals.index("cat")
print(exist)


animals.clear()
print(animals)  # clear everything []

if "cat" in animals:
    print(animals.index("cat"))
else:
    print("cat doesnt exist")


print("-----------------------")
numbers = [2, 5, 23, 213, 12, 323, 23, 12]
numbers.sort()
print(numbers)  # [2, 5, 12, 12, 23, 23, 213, 323]

numbers.sort(reverse=True)
print(numbers)  # [323, 213, 23, 23, 12, 12, 5, 2]


# immutable sorted(immutable)
numbs = [2, 43, 23, 100]
new_numbs = sorted(numbs)  # returnd new list instead, dont modifies in place
print(numbs, new_numbs)


print("========Lambda============")  # small anonymous function!


def calculate(x, y): return x * y


result = calculate(2, 34)
print(result)

people = [
    ("beki", 23),
    ("mike", 45),
    ("john", 25),
    ("noe", 16)
]
people.sort()  # sorted by people names
print(people)


# sort by age via lambda
people.sort(key=lambda person: person[1])
print(people)


print("======== erumerate , map , filter============")
# enumerate for index & value
animals = ["dog", "cat", "fish"]            # List
for ele in enumerate(animals):
    print(ele)

print("-------")
for (index, value) in enumerate(animals):
    print(index, value)

# similar in dict
car_obj = dict(brand="tesla", year=2332)         # Dict
result = car_obj.items()
for (key, value) in result:
    print(key, value)  # brand tesla  year 2332


print("---map----")
# map
cars = [
    ("ferrasri", 23),
    ("toyota", 87),
    ("mazda", 43),
    ("audi", 116),
    ("pagani", 33)
]
result1 = map(lambda car: car[0], cars)
print(result1, type(result1))

new_cars = list(result1)
print(new_cars)


print("----filter---")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(result_filter)
print(list(result_filter))
