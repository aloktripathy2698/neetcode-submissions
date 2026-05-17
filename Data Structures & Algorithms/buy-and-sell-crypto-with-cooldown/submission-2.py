class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]

        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]

        return max(dp[n - 1][0], dp[n - 1][2])

'''
n = 0 -> 0
n = 1 -> 0

3 options -> buy, sell, ignore

if buy:
    helper(i, j) = max(helper(i - 1, j), helper(i - 1, not j) - prices[i])
else:
    helper(i, j) = max(helper(i - 2, not j) + prices[i], helper(i - 1, j)
'''