'''TUPLE
1. What is tuple 
2. unpacking arguments 
3. zip
'''

# print("======what is tuple======")
# # Java/PHP/Node.js => Python list = array
# # Literal\

# numbs = [3, 5, 1, 3]
# print(numbs)
# # constructor function
# letters = list("hello world")
# print(letters)


# fruits = ["apple", "lemon", "cherry", "kiwi"]
# print("before fruits:", fruits)

# fruits[2] = "melon"
# print("after:", fruits)

# # !!!WE can not change tuple (unmutable)
# animals = ("dog", "cat", "fish", "lion")
# tuple_obj = ("mit", 100, True, None)
# print(animals[0])
# animals[0] = "bird"
# print(animals[0])

# print(tuple_obj[2])
# tuple_obj[1] = 22
# print(tuple_obj[2])


# try avoid this and use ()
# people = "anderew", "john"
# animals = "dog",


# print("======Unpacking arguments======")
# groups = ["mit", "flexy", "devex", "mg", "harvward"]
# x, y, *z = groups  # after z everything is list
# print(x, y)
# print(z)  # *list


# ARGS > tuple
def calculate(*args):
    total = 1
    for x in args:
        total *= x
        print(f"type(args):, {type(args)}")
        print(total)

    return total


# call
calculate(4, 3, 3)
print("-------")
calculate(2, 4)


# **kwargs > dictionary
def intoduce(**kwargs):
    print(f"the type of (**kwargs) value:{type(kwargs)}")
    print(f"hi i am{kwargs["name"]} and i am {kwargs["age"]} and my  hobby is {kwargs["hobby"]}")
    pass


# Call
intoduce(name="chris", age=22, hobby="football")
