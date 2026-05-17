class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = float('-inf'), float('-inf')
        for num in nums:
            currSum = max(currSum + num, num)
            maxSum = max(currSum, maxSum)
        return maxSum
        