class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def helper(i, target):
            if i == len(nums):
                if target == 0:
                    return 1
                return 0
            if (i, target) in memo:
                return memo[(i, target)]
            memo[(i, target)] = helper(i + 1, target - nums[i]) + helper(i + 1, target + nums[i])
            return memo[(i, target)]

        return helper(0, target)