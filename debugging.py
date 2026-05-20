'''Packages & Debugging
1. Python Packages & Core Packages 
2. Package Manager & External Package
3. Debugging 
'''

from PIL import Image
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
# my_file = open("material/message.txt", "r")
# try:
#     content = my_file.read()
#     print(content)
# finally:
#     my_file.close()
# # with - Context Manager
# with open("material/message.txt", "r") as your_file:
#     your_content = your_file.read()
#     print(your_content)
# print("Done")


print("======. External Package ======")

# EXTERNAL Packages https://pypi.org/
'''Package Manager > pip (python)
python > pip pipenv 
nodeJS > npm yarn
PHP > composer
MacOS > brew 
'''


# with Image.open("material/me.png") as img_obj:
#     resized_img = img_obj.resize((400, 200))
#     resized_img.show()
#     resized_img.save("material/sample.png")


print("====== Debugging ======")


def get_summary(*args):  # define
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount  # debugging (space bug)


# call
test = 100
print(get_summary(1, 2, 3, 4, 5)) 
