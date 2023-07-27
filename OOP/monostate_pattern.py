# Monostate design pattern is a singleton design pattern variation in which a class will act like a singleton but this class will look like a normal class.
# This design pattern states that all data member of monostate classes are static but any number of instances can be created in the program.

from pprint import pprint

class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


print(Cat)
print(Cat.__dict__)
print()

bob = Cat()
print(bob)
# bob.color = 'white'
print(bob.__dict__)
print()

max = Cat()
print(max)
max.color = 'blue'      # The specifcі a monostate pattern is changing values in all next class instances after the object where were changes.  
max.wild = False        # But not in previous instances. If we set some new attributes, it will also add the same attributes to the next class instances.
print(max.__dict__)     #
print()

tom = Cat()
print(tom)
setattr(tom, 'is_fluffy', True)
print(tom.__dict__)
print()

pop = Cat()
print(pop)
print(pop.__dict__)
print()

pprint(Cat.__dict__)