class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        dp = [[None] * (target + 1) for _ in range(len(nums) + 1)]

        def helper(i, target):
            if target == 0:
                return True
            if i == len(nums):
                return False
            if dp[i][target]:
                return dp[i][target]
            dp[i][target] = helper(i + 1, target - nums[i]) or helper(i + 1, target)
            return dp[i][target]

        return helper(0, target)
        