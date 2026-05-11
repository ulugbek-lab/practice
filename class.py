'''CLASS
1. WHat is class
2. Ordinary vs static properties 
3. Special methods 

'''
print("==============what is class================")
# Class = blueprint for object creation
# structure > state constructor method


class Person():
    # state
    massage = "class static state property"

    # constructor
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
