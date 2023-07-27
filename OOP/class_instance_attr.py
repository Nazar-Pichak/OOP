# Class instance attributes are attributes which belong to the particular instance.

from pprint import pprint

class Car:
    model = 'BMW'
    engine = 1.6

print(Car)
print(Car())
print()

instance_1 = Car()
instance_2 = Car()

print(id(instance_1), id(instance_2))   # There are here two different instances of the <class '__main__.Car'> object and their different memory location.
print(instance_1)
print(instance_2)
print()

pprint(Car.__dict__)            # The attributes of <class '__main__.Car'> object.
pprint(instance_1.__dict__)     # The attributes of instance <class '__main__.Car'> object (so far empty).
pprint(instance_2.__dict__)     # The attributes of instance <class '__main__.Car'> object (so far empty).
print()

print(Car.engine)               # Getting value of attribute from the <class '__main__.Car'> object.           
print(instance_1.model)         # Getting value of attribute the <class '__main__.Car'> object through the instance of this class.
print(instance_2.engine)        # Getting value of the same attribute the <class '__main__.Car'> object through the another instance of this class. 
print()

instance_1.seat = 4                     # Set attributes for the instances of the main class object through assigning  
instance_2.seat = 5                     # 
setattr(instance_1, 'size', '1.5m')     # Set attributes for the instances of the main class object with built-in function setattr()
setattr(instance_2, 'size', '2m')

setattr(instance_1, 'model', 'Audi')    # Set the same names of attributes for class instances like in main class of these instances. 

print(instance_1.__dict__)
print(instance_2.__dict__)
print()

print(Car.model, Car.engine)                                                        # If a class instance has the same name of attribute as a main class, the first interpretter will find
print(instance_1.model, instance_1.engine, instance_1.seat, instance_1.size)        # and return a value of class instance attribute, otherwise it will return the value of main class attribute. 
print(instance_2.model)                                                             # It looks like as a scope and namespace with princip LOCAL —> GLOBAL.




