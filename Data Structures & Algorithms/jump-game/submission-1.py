class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = collections.defaultdict(bool)
        def helper(i):
            if i == len(nums) - 1:
                return True
            if i >= len(nums):
                return False
            if i in memo:
                return memo[i]
            furthestJump = min(i + nums[i], len(nums) - 1)
            for j in range(furthestJump, i, -1):
                if helper(j):
                    memo[j] = True
                    return True
            memo[i] = False
            return memo[i]
        return helper(0)
        