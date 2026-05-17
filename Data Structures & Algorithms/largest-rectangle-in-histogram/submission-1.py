class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, (i - idx) * height)
                start = idx
            stack.append((start, h))
        
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

        