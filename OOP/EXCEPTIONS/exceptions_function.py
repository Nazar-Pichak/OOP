# Exceptions in the functions.
# If we have several functions and a stack call, the execptions will propagate over a whole stack.
# We can hadle this exception on the different levels of stack.

def third():
    print('start third')
    1/0
    print('start third')

def second():
    print('start second')
    third()
    print('finish second')


def first():
    print('start first')
    try:
        second()
    except ZeroDivisionError:
        print('error is handled')
    print('finish first')

print('Nice')
first()