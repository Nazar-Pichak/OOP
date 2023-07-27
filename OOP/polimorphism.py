# Polymorphism is one of the most important concept of OOP.
# The basis of this idea is to avoid repetitions of code and increase reusability of this code. 
# Depending on the class name or instance name here will be called their methods which have the same
# names inside these classes.
# Polymorphism (Greek: πολύς "many" + μορφή "form") is a concept in programming
# and type theory based on the use of a single interface for different types of entities
# or in the use of the same symbol to manipulate data of different types.
# Also polymorphism is a binary operator '+'.
# We can add int + int or int + float or 'string' + 'text' or [1, 2] + [3, 4] 
# and it is also the same interface for the different types of entities. 


from math import pi

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b
    
    def __str__(self):
        return f'The Rectangle is {self.a}x{self.b}'
    
class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a**2

    def __str__(self):
        return f'The Square is {self.a}x{self.a}'
    
class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return pi * self.r ** 2

    def __str__(self):
        return f'The Circle radius is {int(self.r)}'
    

figures_via_class = (Rectangle(2, 3), Square(2), Circle(6), Rectangle(5, 6), Square(7), Circle(9))

for figure in figures_via_class:
    print(figure, f'and his area is {figure.get_area()}')

print()

rect_1 = Rectangle(9, 21)
rect_2 = Rectangle(31, 21)
sqrt_1 = Square(21)
sqrt_2 = Square(11)
circle_1 = Circle(21)
circle_2 = Circle(21)

figures_via_instance = (rect_1, rect_2, sqrt_1, sqrt_2, circle_1, circle_2)
for figure in figures_via_instance:
    print(figure, f'and his area is {figure.get_area()}')