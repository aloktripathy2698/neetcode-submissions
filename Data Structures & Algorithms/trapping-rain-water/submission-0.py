class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])
        ans = 0
        for i in range(len(height)):
            curr = min(maxLeft[i], maxRight[i]) - height[i]
            ans += curr if curr > 0 else 0
        return ans
