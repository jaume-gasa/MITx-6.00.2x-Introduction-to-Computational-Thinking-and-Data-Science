'''
2 Problem 2 (5/5 points)
Using the random module

This problem asks you to write a short function that uses the the random module.
Click on the above link to be taken to the Python docs on the random module,
 where you can see all sorts of cool functions the module provides.

The random module has many useful functions - play around with them in your
interpreter to see how much you can do! To test this code yourself, put the line
import random at the top of your code file, to import all of the functions in
the random module. To call random module methods, preface them with random.,
as in this sample interpreter session:

>>> import random
>>> random.randint(1, 5)
4
>>> random.choice(['apple', 'banana', 'cat'])
'cat'

How would you randomly generate an even number x, 0 <= x < 100? Fill out the
definition for the function genEven(). Please generate a uniform distribution
over the even numbers between 0 and 100 (not including 100).
'''

import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    a = random.randint(0,100)
    print (a)
    while(a % 2 != 0):
        a = random.randint(0,100)
    print (a)

genEven()

''' Otras soluciones

# There are many good answers to this problem, some easier than others :)
def genEven():
    return random.randrange(0, 100, 2)

def genEven():
    return random.choice(range(0, 100, 2))

def genEven():
    return int(random.random() * 50)*2

def genEven():
    return random.choice(range(0, 50))*2

'''