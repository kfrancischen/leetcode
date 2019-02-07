class AdjListNode:
    def __init__(self, v, w):
        self.v = v
        self.w = w

class Graph:
    def __init__(self, numOfV):
        self.numOfVertices = numOfV
        self.adj = [[] for _ in range(numOfV)]

    def addEdge(self, u, v, w):
        node = AdjListNode(v, w)
        self.adj[u].append(node)

    def topologicalSort(self, v, visited, stack):
        visited[v] = True
        for node in self.adj[v]:
            if visited[node.v] == False:
                self.topologicalSort(node.v, visited, stack)
        stack.append(v)

    def longestPath(self, s):
        stack = []
        dist = [float('-inf')] * self.numOfVertices
        visited = [False] * self.numOfVertices
        for i in range(self.numOfVertices):
            if visited[i] == False:
                self.topologicalSort(i, visited, stack)

        dist[s] = 0
        while stack:
            u = stack.pop()
            if dist[u] != float('inf'):
                for i in self.adj[u]:

                    if dist[i.v] < dist[u] + i.w:
                        dist[i.v] = dist[u] + i.w
        return dist


g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 5, 1)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)
s = 1
print g.longestPath(s)
