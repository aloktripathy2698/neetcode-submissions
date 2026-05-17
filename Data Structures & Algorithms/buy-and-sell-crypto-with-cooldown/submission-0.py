class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(i, buying):
            if i >= len(prices):
                return 0
            cooldown = helper(i + 1, buying)
            if buying:
                buy = helper(i + 1, not buying) - prices[i]
                return max(cooldown, buy)
            else:
                sell = helper(i + 2, not buying) + prices[i]
                return max(cooldown, sell)
        
        return helper(0, True)

        