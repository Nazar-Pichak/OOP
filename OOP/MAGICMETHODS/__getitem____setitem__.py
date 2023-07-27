# Special magic(dunder) methods for getting, setting an deleting instance indexes.
# __getitem__, __setitem__, __delitem__

class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __str__(self):
        return str(self.values)
    
    def __getitem__(self, index):
        """This method gets an item of the instance starting with index 1"""
        if 1 <= index <= len(self.values):
            return self.values[index - 1]
        else:
            raise IndexError(f"instance index out of range")

    def __setitem__(self, key, value):
        """This method sets item for the instance which starting with index 1 and extends instance size with None values
        if the index is out of range or current instance"""
        if 1 <= key <= len(self.values):
            self.values[key] = value    
            return self.values
        
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([None] * (diff - 1) + [value])
            return self.values
        

    def __delitem__(self, index):
        """This method deletes item of the instance by index starting with index 1"""
        if 1 <= index <= len(self.values):
            del self.values[index - 1]
            return self.values
        else:
            raise IndexError("object assignment index out of range")

# __getitem__     
v = Vector(12, 34, 56, 23, 23, 11)
print(v.values)
print(v)
print(v[5])
print()

# __setitem__
b = Vector(23, 34)
print(b.values)
print(b)
print(b[1])
b[9] = 18
print(b)
print()

# __delitem__
c = Vector(12, 23, 45, 677)
print(c.values)
print(c)
del c[1]
print(c)


        
