# private_modifier.py

# here we cant directly access or change the balance. 
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def __check_balance(self):  # private method
        print(f"Balance: {self.__balance}")

    def show_balance(self):  # public method to access private balance
        self.__check_balance()

# Example of private access:
account = BankAccount(1000)

# Direct access to private attribute would result in an error
# print(account.__balance)  # This would raise an AttributeError

# Using the public method to access private balance
account.show_balance()  # Works fine

# **Name Mangling (Accessing Private Attributes Outside the Class)**
# Python uses name mangling to alter the name of private variables, making it harder (but not impossible) to access private attributes from outside.

# Accessing private attribute via name mangling
print(account._BankAccount__balance)  # This works but is not recommended
