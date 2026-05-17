class Solution:
    def __init__(self):
        self.ans = []

    def backtrack(self, idx, nums, temp):
        if idx == len(nums):
            self.ans.append(temp.copy())
            return
        temp.append(nums[idx])
        self.backtrack(idx + 1, nums, temp)
        temp.pop()
        self.backtrack(idx + 1, nums, temp)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(0, nums, [])
        return self.ans

        