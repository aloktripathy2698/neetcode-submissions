class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def helper(i):
            if i == len(nums) - 1:
                return True
            if i >= len(nums):
                return False
            furthestJump = min(i + nums[i], len(nums) - 1)
            for j in range(furthestJump, i, -1):
                if helper(j):
                    return True
            return False
        return helper(0)
        