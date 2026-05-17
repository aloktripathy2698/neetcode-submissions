class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = defaultdict(int)

        def helper(i, flag):
            if i >= len(prices):
                return 0
            if (i, flag) in cache:
                return cache[(i, flag)]
            res = helper(i + 1, flag)
            if flag:
                res = max(res, helper(i + 1, not flag) - prices[i])
            else:
                res = max(res, helper(i + 2, not flag) + prices[i])
            cache[(i, flag)] = res
            return res
        return helper(0, True)
        