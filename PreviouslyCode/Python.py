def sayHello():
    print 'hello world'

sayHello()

def printMax(x, y):
    '''Prints the maximum of two numbers.
        ceshi
    The two values must be integers.'''
    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
         print x, 'is maximum'
    else:
         print y, 'is maximum'

print printMax.__doc__


import sys

print 'The commeand line arguments are:'

for i in sys.argv:
    print i
    print '\n \n The PYTHONPATH is', sys.path, '\n'
