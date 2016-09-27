from GraphJaume import *


# Deep First Search
def DFS(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # this prevents cycles
            newPath = DFS(graph, node, end, path)
            if newPath is not None:
                return newPath
    return None

nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]
g = Graph()
for node in nodes:
    g.addNode(node)
edges = [[0, 1], [0, 2], [1, 4], [2, 3], [4, 5], [3, 5]]
for edge in edges:
    g.addEdge(Edge(nodes[edge[0]], nodes[edge[1]]))
path = DFS(g, nodes[3], nodes[1])
index = 0
for p in path:
    for node in nodes:
        if p is node:
            print index
        index += 1
    index = 0
