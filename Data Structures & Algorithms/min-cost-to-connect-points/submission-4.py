class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.conns = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        self.conns -= 1
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

    def connections(self):
        return self.conns - 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calculate_distance(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        n = len(points)
        dsu = DSU(n)

        edges = []

        for i in range(n - 1):
            for j in range(i + 1, n):
                x, y = points[i], points[j]
                d = calculate_distance(x, y)
                edges.append([i, j, d])

        edges.sort(key=lambda x: x[2])

        res = 0
        for u, v, w in edges:
            if dsu.union(u, v):
                res += w
        return res
