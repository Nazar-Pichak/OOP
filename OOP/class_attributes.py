# class attributes

from pprint import pprint

class Person:
    name = 'Nazar'
    age = 26

print(Person)                       # <class '__main__.Person'> main person object            
print(Person.name)                  # getting access to the value of attribute
print(Person.age)
Person.age = 10                     # changing value of attribute
print(Person.age)                           
pprint(Person.__dict__)             # mappingproxy object for getting all attributes of particular object
print()

print(getattr(Person, 'name'))              # getting access to the value of attribute via function getattr()   
print(getattr(Person, 'age'))               
print(getattr(Person, 'anonymous', None))   # returning default's value of indefinite attribute 
print()

Person.address = 'New-yourk'                # set dynamically a new attribute to the object 
print(Person.address)                       
Person.address = 'California'               # changing the value of dynamically seted attribute
print(Person.address)
pprint(Person.__dict__)

setattr(Person, 'email', 'person@gmail.com')    # set a new attribute to the object via function setattr()
print(Person.email)
setattr(Person, 'email', 'nazar@gmail.com')     # changing value of a new attribute 
print(Person.email)
pprint(Person.__dict__)

Person.indefinite = 'deleting attribute'
Person.indefinite_ = [1, 2, 3, 4, 5]
pprint(Person.__dict__)

del Person.indefinite
delattr(Person, 'indefinite_')
pprint(Person.__dict__)

Person.telephone = '+043 000 000'

first_instance = Person()           # The attributes of the main class are automatically added to the instances of this class  
second_instance = Person()          # during creation these instances and store them into variables.
first_instance.street = 'Main str.'
second_instance.id = '000234123'    # Adding a new attribute to the main class will automatically add this attribute to the all instances of this class.
pprint(dir(first_instance))         # Also we can delete one attribute from main class and we will lose one attr from each instance of this class.  
pprint(dir(second_instance))        # To add attributes to the instances separately we should turn to the variables of these instances.

print(first_instance.name)
print(second_instance.name)
