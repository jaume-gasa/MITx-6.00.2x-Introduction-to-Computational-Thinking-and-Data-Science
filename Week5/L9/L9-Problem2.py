from GraphJaume import *

'''
Second graders are lining up to go to their next class, but must be ordered
alphabetically before they can leave. The teacher only swaps the positions of
two students that are next to each other in line.

If we want to represent this situation as a graph, which variables should be
represented as edges and vertices?
'''


'''
ABC
    BAC
    ACB
'''


def isAdyacent(s1, s2):
    return (s1[0] == s2[1] and s1[1] == s2[0] and s1[2] == s2[2]) or (s1[0] == s2[0] and s1[1] == s2[2] and s1[2] == s2[1])


def edgeGenerator(graph, nodes):
    for n in nodes:
        for n2 in nodes:
            if n is not n2 and isAdyacent(n.getName(), n2.getName()):
                if not graph.edges.get(n):
                    graph.addEdge(Edge(n, n2))


nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]
g = Graph()
for n in nodes:
    g.addNode(n)
edgeGenerator(g, nodes)
jau = g.childrenOf(nodes[4])
for i in jau:
    print i
