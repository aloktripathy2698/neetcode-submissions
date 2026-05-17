class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(temp, seen):
            if len(nums) == len(temp):
                ans.append(temp.copy())
                return
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                temp.append(nums[i])
                backtrack(temp, seen)
                temp.pop()
                seen.remove(nums[i])
        
        backtrack([], set())
        return ans
