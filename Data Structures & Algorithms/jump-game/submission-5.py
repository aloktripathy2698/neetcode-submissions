class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums) - 1):
            maxReach = max(maxReach, nums[i] + i)
            if i == maxReach:
                return False
        return maxReach >= len(nums) - 1