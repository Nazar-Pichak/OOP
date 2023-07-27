# Using <class 'property'> and his methods(getter, setter, deletter) as a decorator to describe and change behavior of the main class.
# Property decorator uses to add to the class instances methods additional functionality and represent them by additional methods.
# In other words it represents class instances methods using methods of representation(descriptors) <class 'property'> and decorate class instance methods.
# Syntactic sugar is usually a shorthand for a common operation that could also be expressed in an alternate, 
# more verbose, form: The programmer has a choice of whether to use the shorter form or the longer form,
# but will usually use the shorter form since it is shorter and easier to type and read.
# The main thing for <class 'property'> decorator is to use the same names of the class instances methods to convert them all to the type "property" and 
# represent them using property descriptors.
# property() is a class that contains built-in data and none-data descriptors.
# Descriptor is any object that defines __get__, __set__ and __delete__ special methods.
# Also we can write an own-defined class descriptor and define to him descriptor protocol.
# And then use him as we need.   

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        print('get balace')
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        print('set balance')

        if not isinstance(value, (int, float)):
            raise ValueError('A value must be an integer.')
        self.__balance = value
        return self.__balance
    
    @balance.deleter
    def balance(self):
        print('Delete balance')
        del self.__balance
    
    docstring = 'Here is some documentation'

holder = BankAccount('David', 1000)
print(type(property.getter), type(property.setter), type(property.deleter), type(property.fget), type(property.fset), type(property.fdel))
print(dir(property))
print(holder.balance)                 
print(holder.balance)
holder.balance = 20000.99
print(holder.balance)
del holder.balance
holder.balance = 24000
print(holder.balance)



