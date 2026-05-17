class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][1] = 1
        for j in range(1, n + 1):
            dp[1][j] = 1
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
        

'''
if m == 0 and n == 0:
    return 0
if m == 1 and n == 1:
    return 1

helper(i, j) = helper(i - 1, j) + helper(i, j - 1)
'''