# __slots__ via inheritance.
# If a parent class has __slots__ variable it does not mean that a child class will have the same behavior.
# In the class hierarchy __slots__ variable does not inherit from the parent class to the child class.
# If we define a new __slots__ variable in the child class it will extend and inherit the __slots__ variable of parent class.

class Rectangle:
    __slots__ = ('__width', 'heigth')

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width = value
        print('setter called')
        return self.__width 
    
class Square(Rectangle):
    __slots__ = 'color'

    def __init__(self, width, heigth, color):
        super().__init__(width, heigth)
        self.color = color
    
r = Rectangle(4, 7)
print(r.width)
print(r.heigth)

s = Square(3, 4, 'red')
print(s.color)
print(s.width)
