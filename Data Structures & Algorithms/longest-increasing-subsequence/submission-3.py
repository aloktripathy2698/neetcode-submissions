class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = defaultdict(int)

        def helper(i):
            if i in cache:
                return cache[i]
            
            res = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res = max(res, 1 + helper(j))
            cache[i] = res
            return res

        return max(helper(i) for i in range(len(nums)))