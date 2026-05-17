class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        pacific, atlantic = set(), set()

        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c, seen):
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc) and grid[nr][nc] >= grid[r][c] and (nr, nc) not in seen:
                    dfs(nr, nc, seen)

        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        return [[r, c] for r, c in pacific if (r, c) in atlantic]
