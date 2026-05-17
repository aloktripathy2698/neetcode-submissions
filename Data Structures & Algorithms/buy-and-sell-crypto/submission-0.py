class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = prices[0], 0
        for price in prices:
            minPrice = price if price < minPrice else minPrice
            maxProfit = price - minPrice if maxProfit < price - minPrice else maxProfit
        return maxProfit
        