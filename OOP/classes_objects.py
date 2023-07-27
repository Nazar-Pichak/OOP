# objects(data and behavior)
# classes
# class instance
# class — is a template for creating objects in python. Class contains inside a data and a behavior of the objects. 

a = [1, 2, 3]
b = type(a)
print(b)


class Car:
    model = 'BMW'
    engine = 1.6

car1 = Car()    # the different class instances of the same class in different memory location 
car2 = Car()    # the different class instances of the same class in different memory location
car3 = Car()    # the different class instances of the same class in different memory location

type_cars = type(car1), type(car2), type(car3)

print(car1, car2, car3)
print(type_cars)

print(isinstance(car1, Car))
print(isinstance(car2, object))
print(isinstance(Car, object))


