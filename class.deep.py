# OOP 4 Concepts of pyhton

# Encapsulation > public __private _protected
print("==============Encapsulation=================")


class Account():

    description = "the class makes bank account"

    def __init__(self, owner, amount):
        self.__owner = owner  # private
        self.__amount = amount  # private

    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property  # used to get as a state directly
    def holder(self):
        return self.__owner

    @holder.setter  # used to chnage state of an object
    def holder(self, new_owmer):
        print("change ownership:", new_owmer)
        self.__owner = new_owmer

    def change_ownership(self, new_owner):
        print("new_owner", new_owner)
        self.__owner = new_owner


my_account = Account("CHRIS", 1000)
my_account.get_balance()
print("-----------")
my_account.deposit(3500)
my_account.withdraw(500)
my_account.get_balance()
print("------------")





try:
    result = my_account.__amount
    print(result)
except Exception as err:
    print("No target state was found")

# Getter vs Setter
print("current owner before:", my_account.holder)
my_account.holder = "ulugbek"  # state
print(my_account.holder)
