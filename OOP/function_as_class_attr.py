# Function as a class attribute.

from pprint import pprint

class Car:
    model = 'BMW'
    engine = 2.0

    def drive(*args):                    # function as an callable attribute of main class
        print("Lets's go!!!", args)       #

print(Car)
pprint(Car.__dict__)
print()

print(Car.drive)                    # If we are getting or calling function as an attribute of main class,  
print(Car.drive())                  # it will simply named as a function object.
print(getattr(Car, 'drive')())
print()

var_instance = Car()                    # If we are getting a function through the instance of main class, 
print(var_instance.drive)
print(var_instance.drive())             # it will named as a bound method object. If we will call the function via
print(getattr(var_instance, 'drive')()) 
                                        # empty instance of main class and this function does not have any passed arguments,
                                        # it will return an error. To avoid this we must to decorate this function with '@staticmethod' or pass an empty sequence 
                                        # as an optional argument. To bind class instance and bound methond we have to pass argument 'self' like the first argument of method.