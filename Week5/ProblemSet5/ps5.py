# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import *

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here
# describing how you will model this problem as a graph.

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#


def load_map(mapFilename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    print "Loading map from file..."
    g = WeightedDigraph()
    with open(mapFilename) as f:
        for line_terminated in f:
            line = line_terminated.rstrip('\n')
            data = line.split(' ')
            nodeSrc = Node(data[0])
            nodeDest = Node(data[1])
            e = WeightedEdge(nodeSrc, nodeDest, data[2], data[3])
            try:
                g.addNode(nodeSrc)
                g.addNode(nodeDest)
                t = (float(data[2]), float(data[3]))
                g.edges[nodeSrc].append([nodeDest, t])
            except ValueError:
                t = (float(data[2]), float(data[3]))
                g.edges[nodeSrc].append([nodeDest, t])
                pass
    return g


def addWeightedCost(actual, weight, maxCost):
    actual += weight
    # if actual > maxCost:
    #    raise ValueError
    return actual


#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#
def DFS(graph, start, end, maxDist, maxOut, allPaths, actualDist=0, actualOut=0, path=[]):
    path = path + [start]
    if Node(start) == Node(end):
        p = (path, actualDist, actualOut)
        allPaths.append(p)
        return
    for data in graph.edges[Node(start)]:  # data = [ndest, (dist, sun)]
        if data[0].getName() not in path:  # this prevents cycles
            actualDist += data[1][0]
            actualOut += data[1][1]
            newPath = DFS(graph, data[0].getName(), end, maxDist, maxOut,
                          allPaths, actualDist, actualOut, path)
            if newPath is not None:
                return newPath
    return None

def getTotDist(tuple):
    return tuple[1]

def minLen(tuple):
    return len(tuple[0])

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """

    allPaths = []
    DFS(digraph, start, end, maxTotalDist, maxDistOutdoors, allPaths)
    if not allPaths:
        return None
    else:
        short = len(min(allPaths, key=minLen)[0])
        shortestPaths = []
        for p in allPaths:
            if len(p[0]) == short:
                shortestPaths.append(p)
        return min(shortestPaths, key=getTotDist)[0]


#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#

def DFSopti(graph, start, end, maxDist, maxOut, actualDist=0, actualOut=0, path=[], bestPath=None):
    path = path + [start]
    if Node(start) == Node(end):
        return path
    for data in graph.edges[Node(start)]:  # data = [ndest, (dist, sun)]
        if data[0].getName() not in path:  # this prevents cycles
            if bestPath is None or len(path) < len(bestPath):
                try:
                    actualDist += data[1][0]
                    actualOut += data[1][1]
                    if actualDist > maxDist or actualDist > maxOut:
                        raise ValueError
                    newPath = DFSopti(graph, data[0].getName(), end, maxDist, maxOut,
                                      actualDist, actualOut, path, bestPath)
                    if newPath is not None:
                        bestPath = newPath
                except ValueError:
                    pass
    return bestPath



def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """

    return DFSopti(digraph, start, end, maxTotalDist, maxDistOutdoors)



# Uncomment below when ready to test
# NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
    #    #  Test cases
    '''
        print isinstance(mitMap, Digraph)
        print isinstance(mitMap, WeightedDigraph)
        nodes = mitMap.nodes
        edges = mitMap.edges
        print edges
    '''
    mitMap = load_map("mit_map.txt")
    LARGE_DIST = 1000000

    ##  Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)


'''
    ##  Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)
    # Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)
    print "---------------"
    print "Test case 3:"
    #  Test case 3
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
    print "DFS: ", dfsPath3
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)
   #  Test case 4
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
    dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
    print "DFS: ", dfsPath4
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)
   #  Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)
   #  Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)
   #  Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'
        try:
            directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
        except ValueError:
            dfsRaisedErr = 'Yes'
            print "Expected: No such path! Should throw a value error."
            print "Did brute force search raise an error?", bruteRaisedErr
            print "Did DFS search raise an error?", dfsRaisedErr
           #  Test case 8
            print "---------------"
            print "Test case 8:"
            print "Find the shortest-path from Building 10 to 32 without walking"
            print "more than 100 meters in total"
            bruteRaisedErr = 'No'
            dfsRaisedErr = 'No'
            try:
                bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
            except ValueError:
                bruteRaisedErr = 'Yes'
                try:
                    directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
                except ValueError:
                    dfsRaisedErr = 'Yes'
                    print "Expected: No such path! Should throw a value error."
                    print "Did brute force search raise an error?", bruteRaisedErr
                    print "Did DFS search raise an error?", dfsRaisedErr
'''
