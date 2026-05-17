import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        wt = collections.Counter(t)
        have, need = 0, len(wt)
        ws = collections.defaultdict(int)
        l, ansLen, ans = 0, math.inf, [-1, 1]
        for r in range(len(s)):
            ws[s[r]] += 1
            
            if s[r] in wt and ws[s[r]] == wt[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < ansLen:
                    ans = [l, r]
                    ansLen = r - l + 1
                ws[s[l]] -= 1
                if ws[s[l]] < wt[s[l]]:
                    have -= 1
                l += 1
        l, r = ans
        return s[l: r + 1] if ansLen != math.inf else "" 

                

        
            
        