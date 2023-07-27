# Inheritance is one of four concepts OOP.
# Languages that support classes almost always support inheritance. 
# This allows classes to be arranged in a hierarchy that represents "is-a-type-of" relationships.
# For example, class Employee might inherit from class Person.
# All the data and methods available to the parent class also appear in the child class with the same names.
# For example, class Person might define variables "first_name" and "last_name" with method "make_full_name()".
# These will also be available in class Employee, which might add the variables "position" and "salary". 
# This technique allows easy re-use of the same procedures and data definitions, in addition to potentially mirroring real-world relationships in an intuitive way. 
# Rather than utilizing database tables and programming subroutines, the developer utilizes objects the user may be more familiar with: objects from their application domain.[22]
# 

# parent class or base class
class Person:
    def can_breath(self):
        print('I can breath')

    def can_walk(self):
        print('I can walk')

# child class or subclass
class Doctor(Person):
    def can_cure(self):
        print('I can treat')

# child class or subclass for class Doctor.
class Oftalmolog(Doctor):
    def check_vision(self):
        print('I can check a vison')
        

# child class or subclass
class Builder(Person):
    def can_build(self):
        print('I can build')


d = Doctor()
b = Builder()
o = Oftalmolog()

print(issubclass(Builder, Person))
print(issubclass(Doctor, Person))
print(issubclass(Doctor, Builder))
print()
print(isinstance(b, Builder))
print(isinstance(b, Person))
print(isinstance(d, Doctor))
print(isinstance(d, Person))
print()
print(issubclass(Oftalmolog, Person))
print(issubclass(Oftalmolog, Doctor))
print(issubclass(Oftalmolog, Builder))
