# Inheritance and method overriding.
# Method overrding allows a child class to provide a specific implementation of a method that is already provided by one of its parent class.
# For each child class attributes and methods are lookup in this class, if there is no such attribute or method in child class, then it will lookup in the parent class.
# Also we can override magic methods.  

class Person:
    def __init__(self, name):
        print('__init__ Person')
        self.name = name

    def breath(self):
        print('Human can breath')

    def walk(self):
        print('Human can walk')

    def sleep(self):
        print('Human can sleep')

    def combo(self):
        self.breath()
        self.walk()
        self.sleep()

    def __str__(self):
        return f'Person {self.name}'


class Doctor(Person):

    def breath(self):
        """Here child class overrides the method of parent class"""
        print('Doctor walks via overridden method')

    def __str__(self):
        return f'Doctor {self.name} via overridden magic method'

p = Person('Anonymous')
d = Doctor('Alban')
print(p.breath())
print(p.walk())
print(d.breath())
print(d.walk())
print()
print(p)
print(d)
print()
print(p.combo())
print(d.combo())


