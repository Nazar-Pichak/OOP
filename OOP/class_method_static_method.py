# Class classmethod and Class staticmethod

# A staticmethod transform a method into a static method.
# A static method does not receive an implicit first argument.
# Static method objects provide a way of defeating the transformation of function objects to method objects described above.
# A static method object is a wrapper around any other object, usually a user-defined method object.
# When a static method object is retrieved from a class or a class instance, the object actually returned is the wrapped object,
# which is not subject to any further transformation. Static method objects are also callable.
# Static method objects are created by the built-in staticmethod() constructor. The staticmethod object does not bind neither to class nor class instance.

# A class method object, like a static method object, is a wrapper around another object that alters the way in which that object is retrieved from classes and class instances.
# The behaviour of class method objects upon such retrieval is described above, under “User-defined methods”. 
# Class method objects are created by the built-in classmethod() constructor.

print(staticmethod)
print(classmethod)

class Example:
    def greeting():
        print('Hello here!')

    def instance_greeting(self):
        print(f'Hello from the class instance {self}')

    @staticmethod
    def staticmethod():
        print('Hello from staticmethod')

    @classmethod
    def classmethod(cls):
        print(f'Hello from the classmethod {cls}')


x = Example()
Example.staticmethod()
x.staticmethod()
print()
Example.classmethod()
x.classmethod()
print()

print(dir(Example))
print(dir(x))
print()

print(Example.__dict__)
print(x.__dict__)
print(Example.__class__)
print(x.__class__)