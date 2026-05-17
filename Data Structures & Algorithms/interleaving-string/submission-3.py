from collections import defaultdict

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = defaultdict(bool)

        def helper(p1, p2):
            p3 = p1 + p2

            if p3 == len(s3):
                return p1 == len(s1) and p2 == len(s2)

            if (p1, p2) in memo:
                return memo[(p1, p2)]

            res = False
            if p1 < len(s1) and s1[p1] == s3[p3]:
                res |= helper(p1 + 1, p2)
            if p2 < len(s2) and s2[p2] == s3[p3]:
                res |= helper(p1, p2 + 1)
            memo[(p1, p2)] = res
            return memo[(p1, p2)]

        return helper(0, 0)
            