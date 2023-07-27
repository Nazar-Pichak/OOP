# Delegating procces uses super() function to call the methods of a parent class from a child class.
# Delegating helps to avoid code repetitions and reuse the same code and methods of parent class. 

class Person:
    def __init__(self, name=None, surename=None):
        self.name = name
        self.surename = surename

    def print_data(self):
        return f'{self.name} {self.surename}'
    
    def __str__(self):
        return f'Person {self.name} {self.surename}'

class Doctor(Person):

    def __init__(self, age, name=None, surename=None):
        super().__init__(name, surename)
        self.age = age

    def print_data(self):
        return f'{super().print_data()} {self.age}'
    
    def __str__(self):
        return f'Doctor {self.name} {self.surename} is {self.age} years old'

p = Person()
d = Doctor(12, 'Alex', 'Morrison')
print(p.print_data())
print(d.print_data())
print(p, d)

