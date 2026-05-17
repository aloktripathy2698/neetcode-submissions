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
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return False
        
        self.comps -= 1
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[y_parent] > self.rank[x_parent]:
            self.parent[x_parent] = y_parent
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1
        return True

    def get_components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)

        for x, y in edges:
            if not dsu.union(x, y):
                return False
        return dsu.get_components() == 1
        