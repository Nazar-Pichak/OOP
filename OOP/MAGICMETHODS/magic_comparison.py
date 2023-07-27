# Special magic(dunder method) methods of comparison.
# object.__lt__(self, other) is equivalent to x < y 
# object.__le__(self, other) is equivalent to x <= y
# object.__eq__(self, other) is equivalent to x == y
# object.__ne__(self, other) is equivalent to x != y
# object.__gt__(self, other) is equivalent to x > y
# object.__ge__(self, other) is equivalent to x >= y

# In practice one comparison method can replace two method and give opposite value.

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print('__eq__ method call')
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print('__lt__ method call')
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other
        
    def __le__(self, other):
        print('__le__ method call')
        return self == other or self < other
        

firs_rec = Rectangle(1, 5)
second_rec = Rectangle(1, 5)
print(firs_rec == second_rec)
print(firs_rec != second_rec)
print(firs_rec < second_rec)
print(firs_rec > second_rec)
print(firs_rec >= second_rec)
print(firs_rec >= second_rec)