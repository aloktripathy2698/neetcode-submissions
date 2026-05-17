class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        sp, sa = set(), set()

        def dfs(r, c, seen):
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if heights[nr][nc] >= heights[r][c] and (nr, nc) not in seen:
                        dfs(nr, nc, seen)

        for r in range(rows):
            dfs(r, 0, sp) 
            dfs(r, cols - 1, sa)

        for c in range(cols):
            dfs(0, c, sp)
            dfs(rows - 1, c, sa)

        return [[r, c] for r, c in sp if (r, c) in sa]
