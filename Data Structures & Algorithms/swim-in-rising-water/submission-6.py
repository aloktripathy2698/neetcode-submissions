from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = grid[0][0]
        minHeap = [(dist[0][0], 0, 0)] # (d, r, c)

        while minHeap:
            d, r, c = heappop(minHeap)

            if d > dist[r][c]:
                continue

            if r == rows - 1 and c == cols - 1:
                return d

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    nd = max(d, grid[nr][nc])
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        heappush(minHeap, (nd, nr, nc))
        