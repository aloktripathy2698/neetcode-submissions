class DSU:
    def __init__(self, edges):
        self.parent = defaultdict(int)
        self.rank = defaultdict(int)
        for u, v in edges:
            self.parent[u] = u
            self.parent[v] = v
            self.rank[u] = 1
            self.rank[v] = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_parent, y_parent = self.find(x), self.find(y)

        if x_parent == y_parent:
            return False

        if self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        else:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(edges)
        edge = None
        for u, v in edges:
            if not dsu.union(u, v):
                edge = [u, v]
        return edge
        