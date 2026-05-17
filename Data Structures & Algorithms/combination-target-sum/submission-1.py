class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtrack(idx, temp, curr):
            if idx == len(nums):
                return
            if curr == target:
                ans.append(temp.copy())
                return
            for i in range(idx, len(nums)):
                if curr + nums[i] <= target:
                    temp.append(nums[i])
                    backtrack(i, temp, curr + nums[i])
                    temp.pop()
        
        backtrack(0, [], 0)
        return ans