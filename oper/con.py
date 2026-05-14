'''OPERATORS AND CONDITION

'''
print("===========Operators===========")
a = 34
b = 21
print(a > b)
print(a * b)

result = a // b
left = a % b
print(result)
print(left)

a += 100
print("a:", a)


print(b**2)  # ^2
print(b**3)  # ^3


print("="*10)

c = dict(name="chris", age=22)
d = dict(name="chris", age=22)
e = c
print(c == d)
print(id(c), id(d))  # value is compared not reference or Id

print(e is c)  # true
print(d is c)  # false


print("=========Condition========")
x = 65
if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("case C")
print("=========Logical Operators ========")
age = 19
# person = None
# if(age > 16):
#     person = "adult"
# else:
#     person = "child"
# print(person)


# TERNARY operators
person = "adult" if age > 18 else "minor"
print(person)

print("--------------")
is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("Wanna be a student")
elif is_admin:
    print('Plase go to this office')
elif is_guest or is_parent:
    print("Waiting room is over there")
else:
    print("none")