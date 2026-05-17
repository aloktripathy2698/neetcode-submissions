class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.comps = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_parent, y_parent = self.find(x), self.find(y)

        if x_parent == y_parent:
            return False

        self.comps -= 1
        if self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        else:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += 1
        return True

    def components(self):
        return self.comps
        

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)

        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components() == 1