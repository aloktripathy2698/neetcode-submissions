class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
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
            self.rank[x_parent] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        n = len(points)
        dsu = DSU(n)

        edges = []

        for i in range(n - 1):
            for j in range(1, n):
                x, y = points[i], points[j]
                d = distance(x, y)
                edges.append((d, i, j))

        edges.sort(key=lambda x: x[0])

        res = 0
        for d, u, v in edges:
            if dsu.union(u, v):
                res += d
        return res

