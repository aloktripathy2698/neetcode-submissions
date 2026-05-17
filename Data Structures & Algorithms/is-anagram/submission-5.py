class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        counts = [[0] * 26 for _ in range(2)]
        for i in range(n):
            p1 = ord(s[i]) - ord('a')
            p2 = ord(t[i]) - ord('a')
            counts[0][p1] += 1
            counts[1][p2] += 1
        return counts[0] == counts[1]