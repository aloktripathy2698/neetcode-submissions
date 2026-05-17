class Solution:
    def __init__(self):
        self.ans = []

    def backtrack(self, idx, nums, temp):
        if idx == len(nums):
            self.ans.append(temp.copy())
            return
        self.ans.append(temp.copy())
        for i in range(idx, len(nums)):
            temp.append(nums[i])
            self.backtrack(i + 1, nums, temp)
            temp.pop()


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(0, nums, [])
        return self.ans

        