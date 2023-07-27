# Extending is a procces of adding to the subclass additional methods and attributes
# that are not defined in the parent class. A process of adding the same methods and attributes to the 
# child class as has parent class named 'overriding'.

class Person:
    age = 25

    def breath(self):
        print('Person can breath')

    def sleep(self):
        print('Person can sleep')

    def combo(self):
        self.sleep()
        if hasattr(self, 'walk'):
            self.walk()
        self.breath()
        if hasattr(self, 'age'):
            print(self.age)

class Doctor(Person):
    age = 30

    def sleep(self):
        print('Doctor can sleep')

    def breath(self):
        print('Doctor can breath')

    def walk(self):
        print('Doctor can walk')

p = Person()
d = Doctor()
print(p.sleep())
print(d.sleep())
print(p.breath())
print(d.breath())
print('-' * 20)
d.combo()
p.combo()