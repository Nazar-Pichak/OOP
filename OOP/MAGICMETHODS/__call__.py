# Callable class instance.
# Special magic(dunder) callable method __call__.
# This method can add callable behavior to the instance variable.
# The behavior is the same as a closure in functions and we can pass some arguments 
# into this callable instance variable.

class Counter:
    def __init__(self):
        self.counter = 0
        self.sum = 0
        self.length = 0
        print('__init__ method call')

    def __call__(self, *args, **kwds):
        self.counter += 1
        self.sum = sum(args)
        self.length = len(args)
        print(args, kwds)
        return f'Our instance has called {self.counter} times'

    def average(self):
        print('call avarage')
        return self.sum / self.length


callable_var = Counter()
print(callable_var)

print(callable_var(1, 2, 3, 3, 4, 9))
print(callable_var.average())
print(callable_var(7, 2, 3, 2, 3))
print(callable_var.average())
print(callable_var(1, 4, 3))
print(callable_var.average())
print(callable_var.counter)
print(callable_var.sum)
print(callable_var.length)
