# Special magic(dunder) method __bool__.
# # We can create own-defined object and pass to him appropriate behavior with this methods.

# If a class does not have defined methods __len__ or __bool__, then a boolean value 
# of the class and instance always be True.
 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = Point(12, 34)
print(bool(obj))
print(bool(Point(0, 0)))

class BooleanPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__ call')
        return abs(self.x - self.y)
    
    def __bool__(self):
        print('__bool__ call')
        return self.x != 0 or self.y != 0
    

bool_obj = BooleanPoint(12, 31)
print(bool(bool_obj))
print(bool(BooleanPoint(10, 10)))
print(bool(BooleanPoint(-10, -10)))
print(bool(BooleanPoint(-11, -10)))
print(bool(BooleanPoint(0, -10)))
print(bool(BooleanPoint(-11, 0)))
print(bool(BooleanPoint(0, 0)))

implicitly_True = BooleanPoint(1, 2)
if implicitly_True:
    print(f'Here is the True value from the point {implicitly_True}')

implicitly_False = BooleanPoint(0, 0)
if implicitly_False:
    print(None)