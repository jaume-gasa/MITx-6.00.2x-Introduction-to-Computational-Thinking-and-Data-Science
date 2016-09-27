'''
L2 Problem 3A

Write a deterministic program, deterministicNumber, that returns an even number
between 9 and 21.

'''
import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed(14)
    '''
    El 2 del final son pasos:
        con 9 como primer argumento: [9,11,13,15,17,19,21]
        con 10 : [10,12,14,16,18,20] --> Esto es lo que queremos
    '''
    return random.randrange(10,21,2)



'''
L2 Problem 3B

Write a uniformly distributed stochastic program, stochasticNumber, that returns
an even number between 9 and 21.

'''

def stochasticNumber():

    j = int(random.uniform(9,21))
    while(j % 2 != 0):
        j = int(random.uniform(9,21))
    return j

'''
# Possible solutions:
def stochasticNumber():
    return 2 * random.randint(5, 10)

# or

def stochasticNumber():
    return random.randrange(10, 22, 2)
'''
