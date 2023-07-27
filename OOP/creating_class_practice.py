# Practice with creating a class, Point(x, y)

from math import sqrt

class Point:

    list_points = []

    def __init__(self, x=0, y=0):       # DRY-princip. Do not repeat yourself.
        self.move_to(x, y)              #
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f"The point with cordinates ({self.x}, {self.y})")

    def calc_dist(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('The argument must to be an instance of class Point')
        return sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)

p1 = Point()
p2 = Point(-23, -12)

print(p1.__dict__)
print(p2.__dict__)
print()

p1.move_to(5, 9)
p2.move_to(-3, -9)

print(p1.__dict__)
print(p2.__dict__)
print()

p1.go_home()
p2.go_home()

print(p1.__dict__)
print(p2.__dict__)

p1.print_point()
p2.print_point()
print()

p1.move_to(10, 30)
p2.move_to(23, 20)

print(p1.__dict__)
print(p2.__dict__)
print(p1.calc_dist(p2))

p3 = Point(23, 45)
p4 = Point(23, 35)
p5 = Point(63, 45)
p6 = Point(23, 15)

print(Point.list_points)

for i in Point.list_points:
    print(i.x, i.y)
