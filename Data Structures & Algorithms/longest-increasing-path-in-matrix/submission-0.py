class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        memo = {}

        def dfs(r, c, prevVal):
            if r < 0 or r == rows or c < 0 or c == cols or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            res = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    res = max(res, 1 + dfs(nr, nc, matrix[r][c]))
            memo[(r, c)] = res
            return res

        res = 0
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)
        return max(memo.values())


        

'''
n X n == 0 X 0 -> 0
n == 1 X 1 -> 1

for dr, dc in direction:
    if nr in rows and nc in cols and grid[nr][nc] > grid[r][c]:
        res = max(res, 1 + dfs(nr, nc))
return res
'''