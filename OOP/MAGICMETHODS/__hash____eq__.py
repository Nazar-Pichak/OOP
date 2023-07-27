# Special magic(dunder) methods __hash__, __eq__.
# When we override magic methods we can lose some functionaity of this class and some other 
# magic methods cannot work as previosly.
# Here we override magic-method __eq__ and we lose functionality of another method __hash__.
# To avoid this we have to override lost magic-method inside of this child class.

class Point:
    # pass
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x \
        and self.y == other.y
    
    def __hash__(self):
        return abs(hash((self.x, self.y)))

    
obj = Point(10, 19)
print(dir(Point))
print(dir(obj))
print(obj.__hash__())
print(Point.__hash__(obj))
print(hash(obj))
print(hash(Point))