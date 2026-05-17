class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
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

        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent

        elif self.rank[x_parent] == self.rank[y_parent]:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1
        
        return True

class Solution:

    def manhattan_distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)

        edges = []

        for i in range(n - 1):
            for j in range(1, n):
                p1, p2 = points[i], points[j]
                d = self.manhattan_distance(p1, p2)
                edges.append([d, i, j])
        
        edges.sort()
        res = 0
        for d, u, v in edges:
            if dsu.union(u, v):
                res += d
        return res



        