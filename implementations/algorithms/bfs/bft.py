from collections import defaultdict
import queue


class Graph:
    def __init__(self, isDirtected=False):
        self._isDirected = isDirtected
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if self._isDirected:
            self.graph[v].append(u)

    def bft(self, start):
        # O(V + E), V is the number of vertices, E is the number of edges
        # If graph is connected, only need to start from a vertex
        visited = set()
        vertice_queue = []
        visited.add(start)
        vertice_queue.append(start)
        while len(vertice_queue) != 0:
            current = vertice_queue.pop(0)
            print(current, end=' ')
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    vertice_queue.append(neighbor)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.bft(2)
