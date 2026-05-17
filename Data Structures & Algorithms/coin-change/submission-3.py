class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float("inf")] * (amount + 1) for i in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][amount] if dp[n][amount] != float("inf") else -1


        


# if n == 0:
#     return 0
# if amount == 0:
#     return float("inf")


# f(n, amount) = min(
#     1 + f(n - 1, amount - coins[i - 1]),
#     f(n - 1, amount)
# )