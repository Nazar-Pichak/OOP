# Callable class instance.

from time import perf_counter

class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwds):
        start = perf_counter()
        print(f'Calling function {self.fn.__name__}')
        result = self.fn(*args)
        finish = perf_counter()
        print(f'The function worked {finish - start} seconds')
        return f'The result is {result}'

@Timer
def iter_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(iter_factorial)
print(iter_factorial(6))
print()

def rec_factorial(n):
    if n == 0:
        return 1
    return n * rec_factorial(n - 1)

print(Timer(rec_factorial)(6))     # Special decorating for recursive functions. Not full decorated function
print()

def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + (n - 2)

print(Timer(fib)(7))

