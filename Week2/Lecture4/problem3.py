
import math

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float('Nan')
    micro = 0
    for i in L:
        micro += len(i)
    micro = micro/float(len(L))
    N = len(L)
    result = 0
    for t in L:
        result += (((len(t) - micro)**2)/N)

    return math.sqrt(result)

print stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])
