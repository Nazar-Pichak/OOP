# In Python all exceptions are classes that derived from the class BaseException.
# In the exception's hierarchy it is a main parent class.
# To catch exceptions in python there is an exception handler.
# This is a construction (try: except:). To raise an exception we use keyword 'raise'
# and pass there a class of exception and additional information about this error.

print("Hello1")
print("Hello2")
print("Hello3")
try:
    a = int(input())
except:
    raise ValueError('irregular input value')
print("Hello4")
print("Hello5")
print("Hello6")