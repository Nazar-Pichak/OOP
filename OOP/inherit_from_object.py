# Everithing in Python is an object. All objects which do not have inheritance syntax, by default, are inherited from base class 'object'.
# This base class of the class hierarchy 'object' defines a basic behavior for all new objects and contains a list of basic magic-methods.
# In other words all objects(built-in and user-defined) in Python are inherited from base class 'object' and they are instances and subclasses of this base class.
# The chain of inheritance is infinit and each child class can inherit a behavior and methods of parent class.

import math

class Person(object):
    pass

class Doctor(Person):
    pass

class Architector(Person):
    pass

a = object()
b = Person()
c = Doctor()
print(dir(a))
print(dir(b))
print(dir(c))
print()


# inheritance from built-in objects
class MyList(list):
    def my_additional_method(self):
        print('Here is addtional functionality')

l = MyList()
print(dir(list))
print(dir(l))
print(isinstance(l, object))
print(isinstance(l, list))
print(isinstance(l, MyList))
print()

