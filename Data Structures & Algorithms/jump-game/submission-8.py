class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReachable = 0
        for i in range(len(nums) - 1):
            if maxReachable < i:
                return False
            maxReachable = max(maxReachable, i + nums[i])
        return maxReachable >= len(nums) - 1