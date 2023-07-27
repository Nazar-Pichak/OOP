# By definition, a method is a function that is bound to an instance of a class.

from pprint import pprint

class Request:

    def send():
        print('Sent some request.')

print(Request.send)
print(type(Request.send))
print(Request.send())
pprint(Request.__dict__)

http_request = Request()
print(http_request.send)
print(type(http_request.send))

print(type(Request.send) is (http_request.send))

'''So the http_request.send is not a function like Request.send. 
The following checks if the Request.send is the same object as http_request.send.
It'll returns False as expected:'''

# the http_request.send is a method that is bound to the http_request object,
# Python always implicitly passes the object to the method as the first argument.
# print(http_request.send()) will return an error: send() takes 0 positional arguments but 1 was given.
# The following redefines the Request class where the send function accepts a list of arguments:

class Request:
    def send(*args):
        print('Sent some content...', args)

print(Request.send())
print()

http_request = Request()

print(hex(id(http_request)))
http_request.send()
print()

http_request.send()
Request.send(http_request)

class Request:
    def send(self):
        print('Sent', self)


"""The following illustrates that the object that calls the send() method,
 is the one that Python implicitly passes into the method as the first argument"""
 
new_request = Request()
print(Request.send(new_request) is new_request.send())

