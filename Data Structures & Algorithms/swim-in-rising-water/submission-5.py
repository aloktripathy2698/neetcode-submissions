from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        INF = 2 ** 31 - 1
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dist = [[INF] * cols for _ in range(rows)]
        dist[0][0] = grid[0][0]
        minHeap = [(grid[0][0], 0, 0)]
        while minHeap:
            d, r, c = heappop(minHeap)
            if dist[r][c] < d:
                continue
            if r == rows - 1 and c == cols - 1:
                return d
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_d = max(d, grid[nr][nc])
                    if new_d < dist[nr][nc]:
                        dist[nr][nc] = new_d
                        heappush(minHeap, (new_d, nr, nc))
