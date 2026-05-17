from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dist = [[float("inf") for _ in range(rows)] for _ in range(cols)]
        dist[0][0] = grid[0][0]

        minHeap = [(grid[0][0], 0, 0)] # (d, r, c)

        while minHeap:
            d, r, c = heappop(minHeap)
            if r == rows - 1 and c == cols - 1:
                return d
            if dist[r][c] < d:
                continue
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    next_d = max(d, grid[nr][nc])
                    if next_d < dist[nr][nc]:
                        dist[nr][nc] = next_d
                        heappush(minHeap, (next_d, nr, nc))
    
