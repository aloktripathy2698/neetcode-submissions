from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist = [[float('inf')] * rows for _ in range(cols)]
        dist[0][0] = grid[0][0]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        minHeap = [(grid[0][0], 0, 0)]
        while minHeap:
            d, ur, uc = heappop(minHeap)
            if d > dist[ur][uc]:
                continue
            if ur == rows - 1 and uc == cols - 1:
                return d
            for dr, dc in directions:
                vr, vc = ur + dr, uc + dc
                if 0 <= vr < rows and 0 <= vc < cols:
                    newDist = max(d, grid[vr][vc])
                    if dist[vr][vc] > newDist:
                        dist[vr][vc] = newDist
                        heappush(minHeap, (newDist, vr, vc))
            