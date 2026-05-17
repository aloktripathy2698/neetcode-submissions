class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        
        q = deque()
        for r in range(rows):
            if grid[r][0] == 'O':
                grid[r][0] = 'T'
                q.append((r, 0))
            if grid[r][-1] == 'O':
                grid[r][-1] = 'T'
                q.append((r, cols - 1))

        for c in range(cols):
            if grid[0][c] == 'O':
                grid[0][c] = 'T'
                q.append((0, c))
            if grid[-1][c] == 'O':
                grid[-1][c] = 'T'
                q.append((rows - 1, c))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows 
                    and 0 <= nc < cols 
                    and grid[nr][nc] 
                    == 'O'
                ):
                    grid[nr][nc] = 'T'
                    q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'
                elif grid[r][c] == 'T':
                    grid[r][c] = 'O'



        