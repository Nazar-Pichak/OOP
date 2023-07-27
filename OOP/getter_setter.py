# Using buit-in <class 'property'> and his methods(fset, fget, fdel) to describe and change behavior of the main class.
# Class property() is a class that defines descriptor protocol.

print(dir(property))
print(property)

from pprint import pprint

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balace')
        return self.__balance
    
    def set_balance(self, value):
        print('set balance')

        if not isinstance(value, (int, float)):
            raise ValueError('A value must be an integer.')
        self.__balance = value
        return self.__balance
    
    def delete_balance(self):
        print('Delete balance')
        del self.__balance
    
    docstring = 'Here is some documentation'

    """Here is the property of the current class. It creates via class propery inside the class"""

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance, doc=docstring)

holder = BankAccount('Ashley', 1000)
# print(holder.get_balace())
print(holder.set_balance(3000))
# print(holder.get_balace())
holder.delete_balance()
holder.set_balance(2900)
# print(holder.get_balace())
print()

print(holder.__dict__)
pprint(BankAccount.__dict__)
print()

# Here we can check created property of the class and access to the class instance attributes through this property.
print(BankAccount.balance)
print(holder.balance)
del holder.balance
holder.balance = 3890
print(holder.balance)
print(holder.docstring)