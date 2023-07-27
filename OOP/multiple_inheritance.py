# Multiple inheritance allows us to get behavior methods and attributes of two or more parent classes
# and pass it into one child class.
# The most important concept here is a definition of method resolution order and setting the lookup 
# methods in the class hierarchy.
# In the class hierarchy all classes have a method resolution order and the last class for lookup is 
# a base class 'object'.
# When we use delegating with super() during multiple inheritance, the mothod's lookup will be defined 
# with method resolution order as well.
# Delegating can be also implemented via parent class and its method.

class Mother:
    def __init__(self, hair_color):
        self.hair_color = hair_color

    def eyes(self):
        return 'Mom blue eyes'

class Father:
    def __init__(self, skin_color):
        self.skin_color = skin_color

    def eyes(self):
        return 'Dad hazel eyes'

class Child(Father, Mother):        # definition of method resolution order
    def __init__(self, skin_color, hair_color):     
        super().__init__(skin_color)                
        Mother.__init__(self, hair_color)

    def eyes(self):
        return f'My eyes are a mix of {super().eyes()} and {Mother.eyes(self)}'
    
    def __str__(self):
        return f'I have {self.skin_color} skin color and {self.hair_color} hair color'


print(Child.__mro__)                # attribute to get a method resolution order
c = Child('red', 'yellow')
print(c)
print(c.eyes())