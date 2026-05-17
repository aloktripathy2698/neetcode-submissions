class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: # s = abba
        mp = {} # {a: 0, b: 2}
        res = 0 # 2
        l = 0 # 1 + 1 = 2
        for r, c in enumerate(s): # 2, b
            if c in mp:
                l = max(mp[c] + 1, l)
            res = max(res, r - l + 1) # 2 - 2 + 1
            mp[c] = r
        return res
            
        