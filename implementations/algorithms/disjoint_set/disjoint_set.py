# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3843/
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        # O(log N)
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
        # In different sets
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
uf = UnionFind(10)
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
