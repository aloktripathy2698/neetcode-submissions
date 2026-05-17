class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def helper(i, target):
            if i == len(nums):
                if target == 0:
                    return 1
                return 0
            cache[(i, target)] = helper(i + 1, target - nums[i]) + helper(i + 1, target + nums[i])
            return cache[(i, target)]

        return helper(0, target)