# By definition, encapsulation describes the idea of bundling data and methods that work on that data within one unit, like a class in Java. 
# This concept is also often used to hide the internal representation, or state of an object from the outside. This is called information hiding.
# The general idea of this mechanism is simple.
# For example, you have an attribute that is not visible from the outside of an object.
# You bundle it with methods that provide read or write access.
# Encapsulation allows you to hide specific information and control access to the internal state of the object.
# Python has three levels of accessibility to the internall data attributes.
# These are PUBLIC, PROTECTE and PRIVATE attributes and methods.
# In PyPi there is a module 'accessify' and his decorators to handle levels of accessibility.

class BankAccountPublic:
    """Public attributes and methods. We can get access to these attributes and methods outside of the class."""
    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_public_data(self):
        print(self.name, self.balance, self.passport)

public_account = BankAccountPublic('Alex', '€100 000', 'FC 123 234')
print(public_account.print_public_data())
print(public_account.balance)
print(public_account.name)
print(public_account.passport)


class BankAccountProtected:
    """Protected attributes and methods. We can also get access to these attributes and methods but a single underscore (_) prefix makes it private by convention"""
    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def _print_protected_data(self):
        print(self._name, self._balance, self._passport)

protected_account = BankAccountProtected('Mike', '$20 000', 'FE 003 345')
protected_account._print_protected_data()
print(protected_account._name)
print(protected_account._balance)
print(protected_account._passport)


class BankAccountPrivate:
    """Private attributes and methods. Using double underscore as a prefix of attributes we can restrict access to these attributes from outside.
    Here Python will automatically change a name of __attribute into a _class__attribute. This is called the name mangling in Python."""
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def call_private_method_via_bublic(self):
        self.__print_private_data()

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

private_account = BankAccountPrivate('Ashley', '€10 000', 'FR 234 690')

# private_account.__print_private_data()
# print(private_account.__name)
# print(private_account.__balance)
# print(private_account.__passport)

"""We cannot get access to private attributes and methods outside of class via class instance variable. To get access to the private method we have to create 
another bublic method and then call the private method with him inside of the class or call him outside of class via _class__attribute.
To get access to the private attributes outside of the class we have to call _class__attributes"""

print(dir(private_account))
print()

private_account.call_private_method_via_bublic()
print(private_account._BankAccountPrivate__print_private_data())
print(private_account._BankAccountPrivate__name)
print(private_account._BankAccountPrivate__balance)
print(private_account._BankAccountPrivate__passport)
print()


