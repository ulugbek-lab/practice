'''FUNCTIONS
(1) Define vs Call
(2) Parametr vs Argument
(3) Keyword & default argument
(4) Scope 
'''

# print("=====define vs Call=====")
# build in function > print()  type()
# Funtion - reseusable block of code!
# Instead of block{} in JAVA, Python uses indentation(:)!


# DEFINE - paramtr
# def add(a):
#     print(f"whatts up {a}")


# def add2(b):
#     print("add2 is done")
#     return f"hello {b}"


# # CALL - argument
# result = add("Chris")
# print(result)

# result2 = add2("Jake")


print("=======keyword and default argument==========")

# DEFINE


def plus_greet(name, age=100):
    print("function is executed")
    return f"hi {name}, you are {age} years old"


result = plus_greet(name="beki", age=22)
print(result)

result2 = plus_greet("micheal")
print(result2)
