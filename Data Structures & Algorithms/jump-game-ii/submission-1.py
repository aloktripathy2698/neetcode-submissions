class Solution:
    def jump(self, nums: List[int]) -> int:
        start = end = 0
        minJumps = 0
        while end < len(nums) - 1:
            farthest = 0
            for i in range(start, end + 1):
                farthest = max(farthest, i + nums[i])
            start = end + 1
            end = farthest
            minJumps += 1
        return minJumps


        