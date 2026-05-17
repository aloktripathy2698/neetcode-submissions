class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x != self.parent[x]:
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
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for u, v in edges:
            dsu.parent[u], dsu.parent[v] = u, v
            dsu.rank[u], dsu.rank[v] = 1, 1
        
        latest_edge = [-1, -1]
        for u, v in edges:
            if dsu.find(u) == dsu.find(v):
                latest_edge = [u, v]
            else:
                dsu.union(u, v)
        return latest_edge
            
        