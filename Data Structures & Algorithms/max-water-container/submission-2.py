class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        left, right = 0, len(heights) - 1
        while left < right:
            curr = (right - left) * min(heights[left], heights[right])
            maxWater = max(maxWater, curr)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxWater
        