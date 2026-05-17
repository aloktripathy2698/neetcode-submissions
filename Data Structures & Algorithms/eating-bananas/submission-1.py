class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            m = (l + r)//2
            curr = 0
            for pile in piles:
                curr += math.ceil(pile/m)
            if curr <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans


        