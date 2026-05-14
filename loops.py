'''LOOPS 
(1) Operators
(2) Conditions
(3) While
'''
print("======For Operators======")
# Iterable objects > string dict tuple list range map filter
text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="ferrari", year=2026)
range_obj = range(5)

for letter in text:
    print(letter)
print("--------------")
for number in numbs:
    print(number)
print("--------------")
for x in range_obj:
    print(x)
for key in car_obj:
    print(key, car_obj.get(key))
print("----------")
for x in range(1, 20, 5):
    print(x)


print("======Break/Else======")
for x in range(1, 20, 5):  # range(start, stop, step) 1 + 5 = 6 + 5 = 11 + 5 = 16 + 5 = 21
    print(x)
    if (x > 10):
        print("Break Point")
        break
else:
    print("looped Successfully")


print("======While/Loop======")
numb = 40
while numb > 0:
    numb -= 10
    print(numb)

print("----------")
count = 0
while True:
    count += 1
    x = int(input("Find number"))

    if x == 41:
        print(count)
        break
    else:
        print("pls try again")
