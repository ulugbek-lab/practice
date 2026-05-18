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
