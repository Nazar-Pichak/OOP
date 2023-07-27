# Special magic or dunder methods __str__ and __repr__.
# All magic methods Python calls internally.
# These methods represent an object as a string representation.

class Lion:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self):
        return f'The lion has a name {self.name}'
    
    def __str__(self):
        return f'The lion {self.name}'
    

obj = Lion('Wrarr')
print(obj)
print(Lion.__str__(obj))
print(Lion.__repr__(obj))