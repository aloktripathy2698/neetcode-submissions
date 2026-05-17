class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        ans = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            ans[i] = ans[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            ans[i] = ans[i] * left[i]
        return ans

        