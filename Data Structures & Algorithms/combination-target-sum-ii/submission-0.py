class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(idx, curr, temp):
            if curr == target:
                ans.append(temp.copy())
                return
            if idx == len(candidates):
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i - 1] == candidates[i]:
                    continue
                if curr + candidates[i] <= target:
                    temp.append(candidates[i])
                    backtrack(i + 1, curr + candidates[i], temp)
                    temp.pop()
            
        backtrack(0, 0, [])
        return ans