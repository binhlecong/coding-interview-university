from collections import defaultdict


class Graph:
    def __init__(self, isDirtected=False):
        self._isDirected = isDirtected
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if self._isDirected:
            self.graph[v].append(u)

    def dfsUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfsUtil(neighbour, visited)

    def dft(self):
        # O(V + E), V is the number of vertices, E is the number of edges
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                self.dfsUtil(vertex, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.dft()
