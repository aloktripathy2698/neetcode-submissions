class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m + 1):
            dp[r][1] = 1
        for c in range(n + 1):
            dp[1][c] = 1
        for r in range(2, m + 1):
            for c in range(2, n + 1):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m][n]

        

# if m == 1 -> return 1
# if n == 1 -> return 1
# f(i, j) = f(i - 1, j) + f(i, j - 1)