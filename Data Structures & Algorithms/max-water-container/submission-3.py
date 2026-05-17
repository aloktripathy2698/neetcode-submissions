class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) in [0, 1]:
            return 0
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            base = r - l
            height = min(heights[l], heights[r])
            res = max(res, base * height)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
        