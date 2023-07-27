# __init__() — it is a magic method for initializing attributes for class instances.
# The double underscores at both sides of the __init__() method indicate that Python will use the method internally. In other words, you should not explicitly call this method.
# Since Python will automatically call the __init__() method immediately after creating a new object, you can use the __init__() method to initialize the object’s attributes.
# 'self' in the __init__ method marks the variables of class instances, in some languages it marks by 'this' name.
# All methods which start and end with double underscores are named 'magic methods'. Python will call them under the hood. 
# To avoid calling the regular methods we use more effective way, these are magic methods. They are calling internally and automatically.


from pprint import pprint

class Cat:

    def __init__(self, name, breed='pers', age=1, color='white') -> None:
        print("Hello", self, name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        print()

print(Cat)
pprint(Cat.__dict__)
print()

bob = Cat('Bob', 'pers', 20, 'black')
print(bob.__dict__)
print()

nelly = Cat('Nelly')        # If there is a lack of values in the class instance, it will return the values by default.
print(nelly.__dict__)       
