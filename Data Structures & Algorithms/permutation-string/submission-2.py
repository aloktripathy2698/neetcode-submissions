class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        windowS1 = collections.Counter(s1)
        l, r, ans = 0, len(s1), 0
        windowS2 = collections.Counter(s2[: len(s1)])
        while r < len(s2):
            print(windowS1, windowS2)
            if windowS1 == windowS2:
                return True
            else:
                windowS2[s2[l]] -= 1
                if windowS2[s2[l]] == 0:
                    del windowS2[s2[l]]
                windowS2[s2[r]] += 1
                l += 1
                r += 1
        return windowS1 == windowS2

            

        

        