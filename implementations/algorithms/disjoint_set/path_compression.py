# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3880/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        # O(log N)
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        # O(log N)
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def isConnected(self, x, y):
        # O(log N)
        return self.find(x) == self.find(y)


uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4-0
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
uf.union(4, 0)
print(uf.isConnected(1, 5))  # true
print(uf.isConnected(5, 7))  # true
print(uf.isConnected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.isConnected(4, 9))  # true
