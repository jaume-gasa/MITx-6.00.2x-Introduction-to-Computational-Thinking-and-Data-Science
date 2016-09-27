def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
        00
        01
        02
        10
        11
        20
        21
        22
    """
    N = len(items)
    for i in xrange(3**N):
