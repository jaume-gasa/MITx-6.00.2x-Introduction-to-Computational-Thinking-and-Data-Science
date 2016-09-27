'''
 You have a bucket with 3 red balls and 3 green balls. Assume that once you draw
 a ball out of the bucket, you don't replace it. What is the probability of
 drawing 3 balls of the same color?

 Write a Monte Carlo simulation to solve the above problem. Feel free to write a
 helper function if you wish.
'''
import random

def noReplacementSimulation(numTrials):
    allSameColor = 0
    for j in range(numTrials):
        bucket = ['r','r','r','g','g','g']
        drawed = []
        for i in range(3):
            pick = random.randrange(0, len(bucket)-1)
            drawed.append(bucket.pop(pick))
        if drawed == ['r','r','r'] or drawed == ['g','g','g']:
            allSameColor += 1
    return allSameColor/float(numTrials)

noReplacementSimulation(1000)
