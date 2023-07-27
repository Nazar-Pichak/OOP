# Speacil magic(dunder method) methods __add__, __mul__, __sub__, __truediv__.
# These are mathematical methods which are equivalent to arithmetic operators (+, -, *, /).
# These methods belong to numeric objects in Python.
# All arithmetic and bitwice methods must get another one additional argument excep self.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ method call')
        if isinstance(other, BankAccount):
            self.balance += other.balance
            return self.balance
        if isinstance(other, (int, float)):
            self.balance += other
            return self.balance
        return NotImplemented

    def __radd__(self, other):
        print('__radd__ method call')
        return self + other
    
    def __mul__(self, other):
        print('__mul__ method call')
        if isinstance(other, BankAccount):
            self.balance *= other.balance
            return self.balance
        if isinstance(other, (int, float)):
            self.balance *= other
            return self.balance
        if isinstance(other, str):
            self.name += other
            return self.name

user_1 = BankAccount('Alex', 2300)
print(user_1.balance)
print()
user_1 + 100
print(user_1.balance)
print()

user_2 = BankAccount('Ashley', 1000)
print(user_2.balance)
print()
user_2 + 1000
print(user_2.balance)
print()

user_1 + user_2
user_2 + user_1
print(user_1.balance, user_2.balance)
print()

10 + user_1
10 + user_2
print(user_1.balance, user_2.balance)
print()

print(user_1.balance, user_2.balance)
user_2 * 3
user_1 * 3
print(user_1.balance, user_2.balance)
print()

user_1 * 'text'
user_2 * 'text'
print(user_1.name, user_2.name)