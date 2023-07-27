# Speacial magic(dunder) methods to make instance iterable __iter__, __next__.
# We can create own-defined object and pass to him appropriate behavior with this methods.

class IterableMarks:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        print('call __iter__ marks')
        return self
    
    def __next__(self):
       print('call __next__ marks')
       if self.index >= len(self.values):
           raise StopIteration
       letter = self.values[self.index]
       self.index += 1
       return letter
    


class IterableStudent:
    def __init__(self, name, surename, marks):
        self.name = name
        self.surename = surename
        self.marks = marks
        self.index = 0

    def __iter__(self):
        print('call __iter__ student')
        return self.marks
    
    def __next__(self):
        print('call __next__ student')
        if self.index >= len(self.surename):
            self.index = 0
            raise StopIteration
        letter = self.surename[self.index]
        self.index += 1
        return letter


marks = IterableMarks([1, 2, 3, 8, 9, 10, 12])
student_instance = IterableStudent('Mike', 'Tyson', marks)

for i in student_instance:
    print(i)
        
