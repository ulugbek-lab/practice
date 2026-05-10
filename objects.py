'''OBJECT
1. What is object 
2. Iterable object & Range 
3. Dictionary 
4. Error handling system
'''

# import array  # package/module
# import math  # package
# from math import floor, ceil
# print("====what is object====")
# # An object has state and method properties
# # Everything is an object '


# print(type('hello world'))
# print(type(21))
# print(type(True))
# print(type(array))
# print(type(math))


# # Paradigm > Functional Programming & OOP
# # OOP 4 concepts > Abstraction | encapsulation | inheritance | Polimorphism
# result1 = math.floor(97.7)  # Call
# print(result1)
# result1 = math.ceil(97.7)  # Call
# print(result1)


# print("====Iterable Object & Range====")
# # Iterable object > string dict tuple  list range map filter


# range_obj = range(3)  # [0, 3]
# print(range_obj)
# for ele in range_obj:
#     print(ele)


# text = "MIT"
# for letter in text:
#     print(letter)


print("====Dictionary====")
# Dictionary is JSON object!

person = {
    "name": "chris",
    "age": 22,
    "is_married": False
}
person_obj = dict(name="beki", age=22, single=True)
print(person)
print(person_obj)

name = person_obj["name"]
print(name)

# Method:get()
# name = person_obj["name"]
balance = person_obj.get("balance", 213)
hobby = person_obj.get("hobby")
print(hobby)  # result: none
print(balance)


# del person_obj["single"]  # delete
for key in person_obj:
    print(f"{key}: => {person_obj[key]}")
