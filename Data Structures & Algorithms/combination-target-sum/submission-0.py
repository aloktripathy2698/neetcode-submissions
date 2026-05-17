class Solution:
    def __init__(self):
        self.ans = []
    
    def backtrack(self, idx, nums, curr, temp):
        if curr == 0:
            self.ans.append(temp.copy())
            return
        if idx == len(nums) or curr < 0:
            return
        temp.append(nums[idx])
        self.backtrack(idx, nums, curr - nums[idx], temp)
        temp.pop()
        self.backtrack(idx + 1, nums, curr, temp)
        
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.backtrack(0, nums, target, [])
        return self.ans
        