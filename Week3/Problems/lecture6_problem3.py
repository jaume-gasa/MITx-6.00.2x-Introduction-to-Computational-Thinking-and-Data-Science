'''
Consider a similar problem to the Monty Hall problem:

In this problem, instead of 3 doors, 1 car, and 2 goats, instead there are
4 doors, 2 cars and 2 goats.

As in the Monty Hall problem, the player chooses a door, and then the host opens
a door hiding a goat. With simulation or hand calculation, calculate the
probability that switching into a door will lead you to a car.
'''
import random
import pylab
import math

def HostChoseAGoat(hall):
    hostChoice = ''
    while hostChoice != 'g':
        doorWithGoat = random.randint(0,len(hall)-1)
        hostChoice = hall[doorWithGoat]
    return doorWithGoat

def MontyHallRemix(switch):
    hall = ['c','c','g','g']
    playerChoice = random.randint(0,len(hall)-1)
    playerPrize = hall.pop(playerChoice)
    hall.pop(HostChoseAGoat(hall))
    if switch :
        playerNewChoice = random.randint(0,len(hall)-1)
        playerPrize = hall[playerNewChoice]
    return 1 if playerPrize == 'c' else 0

def MonteCarloMontyHallRemix(numTrials, switch):
    carsWined = 0
    for i in range(numTrials):
         carsWined += MontyHallRemix(switch)
    return carsWined

tries = 100000
winsWithSwitch = MonteCarloMontyHallRemix(tries, True)
winsWithoutSwitch = MonteCarloMontyHallRemix(tries, False)
pctWithSwitch = winsWithSwitch * 100 / tries
pctWithoutSwitch = winsWithoutSwitch *100 / tries
pylab.pie([winsWithSwitch, winsWithoutSwitch, tries - winsWithSwitch - winsWithoutSwitch],
# pylab.pie([pctWithSwitch, pctWithoutSwitch],
            labels = ['% of wining with switch', '% of wining without switch', '% of loosing'],
            autopct = '%.2f%%')
pylab.title('Probability that switching into a door will lead you to a car')
pylab.show()
