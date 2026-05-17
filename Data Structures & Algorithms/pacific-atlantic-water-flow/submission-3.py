class Solution:

    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c, seen):
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] >= grid[r][c] and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        dfs(nr, nc, seen)
        
        pacific_cells = set()
        atlantic_cells = set()
        for r in range(rows):
            dfs(r, 0, pacific_cells)
            dfs(r, cols - 1, atlantic_cells)
        for c in range(cols):
            dfs(0, c, pacific_cells)
            dfs(rows - 1, c, atlantic_cells)

        return [list(cell) for cell in pacific_cells if cell in atlantic_cells]
        



        
        
        