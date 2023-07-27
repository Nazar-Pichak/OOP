# calculates property with math operations and hashing some values

class Square:
    def __init__(self, s) -> None:
        self.__side = s
        self.__area = None      # attribute for storing value in hash form 
                                
    @property
    def side(self): 
        return f'The side of {Square} is {self.__side}'
    
    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print('Here is the first calculation of the area')
            self.__area = int(self.side[-1]) ** 2
        return f"The area of the {Square} is {self.__area}"
    

a = Square(6)
print(a.area)
print(a.area)
print()
print(a.side)
a.side = 10
print(a.side)
print()
print(a.area)
print(a.area)
print()

class SquarePerimeter:
    def __init__(self, side) -> None:
        self.__side = side
        self.__hash_attribute = None

    @property
    def side(self):
        return f'The side of {SquarePerimeter} is {self.__side}'
    
    @side.setter
    def side(self, value):
        self.__side = value
        self.__hash_attribute = None

    @property
    def perimeter(self):
        if self.__hash_attribute is None:
            print('Here is the first calculation of the perimeter')
            self.__hash_attribute = int(self.side[-1]) * 4
        return f"The perimeter of the {SquarePerimeter} is {self.__hash_attribute}"
    
b = SquarePerimeter(5)
print(b.side)
print(b.perimeter)
print(b.perimeter)
print()
b.side = 4
print(b.side)
print(b.perimeter)
print(b.perimeter)
