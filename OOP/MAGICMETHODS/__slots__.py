# This class variable can be assigned a string, iterable, or sequence of strings with variable names used by instances.
# __slots__ reserves space for the declared variables and prevents the automatic creation of __dict__ and __weakref__ for each instance.
# With __slots__ definition we can only hadle those attributes that are declared in the  __slots__ variable and restric dynamically creation attributes.
# __slots__ variable helps to save memory space and accelerate processes for the class.

from timeit import timeit

class Point:
    def __init__(self, x, y):
        self.x = y
        self.y = y

p = Point(1, 2)
print(p.__sizeof__() + p.__dict__.__sizeof__())
print(p.__dict__)
p.a = 10
print(p.__dict__)
p.b = [1, 2, 3]
print(p.__dict__)
print()

class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

s = PointSlots(2, 3)
print(s.__sizeof__())
print(s.__slots__)
print(s.x)
print(s.y)
s.y = 100
print(s.y)
del s.y
print(s.__slots__)
s.y = 28
print(s.y)

def make_call_Point():
    a = Point(2, 3)
    a.x = 100
    a.x
    del a.x

def make_call_PointSlots():
    b = PointSlots(2, 3)
    b.x = 100
    b.x
    del b.x

print(timeit(make_call_Point))
print(timeit(make_call_PointSlots))
print(timeit(make_call_PointSlots) < timeit(make_call_Point))