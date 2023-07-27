# Also we can handle several exceptions with error handler by adding another
# 'except' statemantes and error names. During exception handling after the first error 
# a program quits the blok 'try' and handles exception.

try:
    # a + b
    int('string')
    1/0
except ZeroDivisionError:
    print('division by zero is not allowed')
except ValueError:
    print("cannot convert string to number")
except NameError:
    print('name is not defined')

# To hadle all errors with one type of exception we have to pass 
# an exception type which located heigher on the exception hierarchy.

try:
    # a + b
    1 + 'string'
    int('string')
except Exception:
    print('error')


# There is a 'finaly' statemante that we can use with error handler to pass some commands
# which will executed in any situations regardless we have exceptions ot not.

try:
    1/0
except ZeroDivisionError:
    print('cannnot devide by zero')
finally:
    print('end')