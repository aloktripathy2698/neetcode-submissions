class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        dp = [[False] * (target + 1) for _ in range(n + 1)]

        dp[0][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][target]

        