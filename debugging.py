'''Packages & Debugging
1. Python Packages & Core Packages 
2. Package Manager & External Package
3. Debugging 
'''

import turtle

print("======Python Packages & Core, Package ======")
'''Python Packages/Modules:Core, File and External'''
# Core packages > https://docs.python.org/3/library

# Core
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(3)
# t.end_fill

# turtle.done()

print("----------")
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print(content)
finally:
    my_file.close()
# with - Context Manager
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print(your_content)
print("Done")
