topo = []
visited = {}
graph = {
    'a': ['d'],
    'f': ['b', 'a'],
    'b': ['d'],
    'd': ['c'],
}


def dfs(u):
    visited[u] = 1
    for v in graph.get(u, []):
        if visited.get(v, 0) == 1:
            print('Cycle detected')
            return
        if visited.get(v, 0) == 0:
            dfs(v)
    topo.append(u)
    visited[u] = 2


def getBuildOrder():
    for v in graph:
        if visited.get(v, 0) == 0:
            dfs(v)
    topo.reverse()
    print(topo)


getBuildOrder()
