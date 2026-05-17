'''
nums = [-1, 0, 1, 2, -1, 4]
nums = [-1, -1, 0, 1, 2, 4]

[[-1, 0, 1], [-1, -1, 2]]

nums = []
res = []
 len(nums) < 3
    return []


'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        res = [] # [[-1, -1, 2], [-1, 0, 1]]

        def moveLeftPointer(l, r): # l = 2, r = 5
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            return l + 1

        def moveRightPointer(l, r):
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            return r - 1

        def twoSum(idx, l, r): # idx = 1, l = 2, r = 5
            while l < r:
                total = nums[idx] + nums[l] + nums[r] # -1 + -1 + 2 = 0
                if total == 0:
                    res.append([nums[idx], nums[l], nums[r]])
                    l, r = moveLeftPointer(l, r), moveRightPointer(l, r)
                elif total < 0:
                    l = moveLeftPointer(l, r)
                else:
                    r = moveRightPointer(l, r)

        nums.sort() # nums = [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums) - 2): # i = 0, nums[i] = -4
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            twoSum(i, i + 1, len(nums) - 1)
        return res
        