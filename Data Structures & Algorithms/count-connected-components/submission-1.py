class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.comps = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_of_x, parent_of_y = self.find(x), self.find(y)

        if parent_of_x == parent_of_y:
            return False

        self.comps -= 1
        if self.rank[parent_of_x] < self.rank[parent_of_y]:
            self.parent[parent_of_x] = parent_of_y
        elif self.rank[parent_of_x] > self.rank[parent_of_y]:
            self.parent[parent_of_y] = parent_of_x
        else:
            self.parent[parent_of_y] = parent_of_x
            self.rank[parent_of_x] += 1
        return True

    def components(self):
        return self.comps

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for u, v in edges:
            dsu.union(u, v)

        return dsu.components()
        