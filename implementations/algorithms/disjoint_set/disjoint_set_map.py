# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3843/


class UnionFind:
    def __init__(self):
        self.root = {}
        self.rank = {}

    def find(self, x):
        # O(log N)
        if x not in self.root:
            self.root[x] = x
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        # Alerady in the same set
        if rootX == rootY:
            return
        # Init map
        if rootX not in self.rank:
            self.rank[rootX] = 0
        if rootY not in self.rank:
            self.rank[rootY] = 0
        # Join 2 set
        if self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind()
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.isConnected(1, 5))  # true
print(uf.isConnected(5, 7))  # true
print(uf.isConnected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.isConnected(4, 9))  # true
