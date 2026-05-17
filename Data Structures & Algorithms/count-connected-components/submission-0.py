class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return False

        if self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        else:
            self.parent[y_parent] = x_parent
            self.rank[y_parent] += 1
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = UnionFind(n)
        res = n
        for u, v in edges:
            if ds.union(u, v):
                res -= 1
        return res
        