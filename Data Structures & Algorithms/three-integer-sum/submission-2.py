class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. sort
        # 2. remove duplicates
        # 3. Remove duplicates from fixed numbers

        nums.sort()
        ans = []

        def twoSum(i, j, target):
            while i < j:
                if nums[i] + nums[j] > target:
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    ans.append([-target, nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j - 1] == nums[j]:
                        j -= 1
                    i += 1
                    j -= 1

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            target = -nums[i]
            twoSum(i+1, len(nums) - 1, target)
        return ans
