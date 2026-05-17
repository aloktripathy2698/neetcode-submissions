class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        q = deque() # [(0, 0)]
        fresh = 0 # 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0: return 0
                    
        time = 0 # 4
        while q and fresh > 0:
            n = len(q) # 1
            for _ in range(n):
                r, c = q.popleft() # 0, 1
                for dr, dc in directions: # 0, -1
                    nr, nc = r + dr, c + dc # 0, 0
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            q.append((nr, nc))
            time += 1

        print(fresh)
        
        return time if fresh == 0 else -1