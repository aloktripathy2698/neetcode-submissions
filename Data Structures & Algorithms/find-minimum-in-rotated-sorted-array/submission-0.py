class Solution:
    def findMin(self, nums: List[int]) -> int:
        # move left if  nums[0]<nums[m]>nums[-1]
        # move right if  nums[0]<nums[m]<nums[-1]
        ans = float("inf")

        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            ans = min(ans,nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return min(ans, nums[l])
            