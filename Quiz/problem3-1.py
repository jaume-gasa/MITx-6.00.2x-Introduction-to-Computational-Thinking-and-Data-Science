# import random, pylab
'''
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

pylab.plot(sorted(xVals),sorted(yVals))
pylab.show()
'''


def drawing_without_replacement(numOfPicks=3):
    bucket = ['r', 'r', 'r', 'r', 'g', 'g', 'g', 'g']
    picks = []
    for i in range(numOfPicks):
        picked = random.choice(bucket)
        picks.append(picked)
        bucket.remove(picked)
    return picks


def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    sameColor = 0
    for i in range(numTrials):
        picks = drawing_without_replacement()
        if picks == ['r', 'r', 'r'] or picks == ['g', 'g', 'g']:
            sameColor += 1
    return sameColor/float(numTrials)
