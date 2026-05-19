'''Array & Set
1. Array 
2. Set 
3. Specific operators
'''
from array import array
# used for working with big numbers only and it is strict type ,( no mix data )
numbers = array("i", [3, 45, 5, 3, 24, 32, 3, 32, 1, 446])
print(numbers)
numbers.append(100)
numbers.insert(0, 54)
print(numbers)


numbers.remove(446)
numbers.pop()
print(numbers)

del numbers[0:2]
print(numbers)

print("====== set ========")
# set of unique collection without keeping order!
new_numbers = array("i", [3, 45, 5, 3, 24, 45,  32, 3, 45, 32, 1, 446])
numbs_set = set(new_numbers)
print(numbs_set, type(numbs_set))
numbs_set.add(909)
print(numbs_set)


print("=======Specific Operators=======")
# | & - ^
a = {20, 32, 12}
b = {20, 10}
result1 = a | b  # union
result2 = a & b  # same
result3 = a - b  # difference
result4 = a ^ b  # symetric

print(result1)
print(result2)
print(result3)
print(result4)
