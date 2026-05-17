class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ms, mt = [0] * 26, [0] * 26
        n = len(s)
        for i in range(n):
            ps, pt = ord(s[i]) - ord('a'), ord(t[i]) - ord('a')
            ms[ps] += 1
            mt[pt] += 1
        return ms == mt

        