class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = [0] * 26
        b = [0] * 26
        for i in range(len(s)):
            pos1 = ord(s[i]) - ord('a')
            pos2 = ord(t[i]) - ord('a')
            a[pos1] += 1
            b[pos2] += 1
        return a == b


        