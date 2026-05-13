'''CLASS
1. WHat is class
2. Ordinary vs static properties 
3. Special (magic)methods 

'''
print("==============what is class================")
# Class = blueprint for object creation
# structure > state constructor method


class Person():
    # state
    massage = "class static state property"

    # constructor
    # __init___ this special(maigic) method of python is used fro construction
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"the {self.name} says: How are u")

    def tell_age(self):
        print(f"my age is {self.age}!")

    @classmethod  # @classmethod is used for creating static method
    def explain(cls):
        print("class:  static method property executed")


person_obj = Person("chris", 22)
person_obj2 = Person("Beki", 23)
person_obj3 = Person("ulugbek", 43)

# ordinary state property
print(person_obj.name)
print(person_obj2.name)

person_obj3.introduce()


print("===============2. Ordinary vs static properties ===============")
person_mas = Person.massage
print(person_mas)


# static method
Person.explain()


print("===============Special magic methods ===============")
# These methods:
# __init__   __new__  __str__  __call__  __getItem__  __eq__  __len__...


class Car():
    # state
    description = "this class makes cars"

    # constructor
    def __new__(cls, *args):
        print("__init__ is printed")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"{self.name} started the engine")

    def stop_engine(self):
        print(f"{self.name} stopped  the engine")

    def __str__(self):  # is used to define the informal, human-readable string representation of an object such as Tesla object below
        # its a return method
        return f"the car.name {self.name} was produced in {self.year}"

    def __call__(self):  # to call an object as a function such as your_car() method
        print("object called as function")
        return True


my_car = Car("ferrari", 2026)
my_car.start_engine()
my_car.stop_engine()


print("------------")
your_car = Car("tesla", 2121)
print(your_car)

response = your_car()  # object called as function
print(response)

print(dir(__builtins__))