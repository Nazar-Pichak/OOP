# Special magic(dunder method) methods __len__ and __abs__.
# If we use built-in functions it will automatically call magic method for passed object and execute it internally.
# It the object does not have an appropriate magic method the exception will be rised.
# We can interact with magic methods directly.
# To use some built-in function to the object it means that this object must define magic method appropriate to this function.

print(len('text here'))
print('text here'.__len__())
print(abs(-4))
print((-4).__abs__())

class Person:
    def __init__(self, name, surename):
        self.name = name
        self.surename = surename

    def __len__(self):
        return len(self.name + self.surename)
       
peron1 = Person('Alex', 'Morrison')
print(len(peron1))

peron2 = Person('Mike', 'Tyson')
print(len(peron2))
print()

class Range:
    def __init__(self, point_1, point_2):
        self.x = point_1
        self.y = point_2

    def __len__(self):
        return abs(self)
    
    def __abs__(self):
        return abs(self.x - self.y)

r = Range(10, 7)
print(len(r))
print(abs(r))
print()

q = Range(7, 20)
print(len(q))
print(abs(q))






        
