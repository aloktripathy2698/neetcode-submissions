class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxReachable = 0
        for i in range(n - 1):
            if maxReachable < i:
                return False
            maxReachable = max(maxReachable, i + nums[i])
        return maxReachable >= n - 1
        