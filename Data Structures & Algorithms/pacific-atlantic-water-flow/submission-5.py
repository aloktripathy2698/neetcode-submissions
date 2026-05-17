class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        pacific_set = set()
        atlantic_set = set()

        def dfs(r, c, seen):
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] >= grid[r][c] and (nr, nc) not in seen:
                        dfs(nr, nc, seen)
            

        for r in range(rows):
            dfs(r, 0, pacific_set)
            dfs(r, cols - 1, atlantic_set)

        for c in range(cols):
            dfs(0, c, pacific_set)
            dfs(rows - 1, c, atlantic_set)

        return [[r, c] for r, c in pacific_set if (r, c) in atlantic_set]
        