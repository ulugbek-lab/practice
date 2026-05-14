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
print(id(c), id(d)) # value is compared not reference or Id

print(e is c)# true 
print(d is c)# false