class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxLen = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            curr = 1
            while num + 1 in numSet:
                curr += 1
                num += 1
            maxLen = max(maxLen, curr)
        return maxLen
        