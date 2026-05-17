from collections import defaultdict

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 + s2 == s3:
            return True

        if len(s1) + len(s2) != len(s3):
            return False

        memo = defaultdict(bool)

        def helper(p1, p2, p3):
            if p3 == len(s3):
                return True
            if (p1, p2, p3) in memo:
                return memo[(p1, p2, p3)]
            if p1 < len(s1) and p2 < len(s2):
                if s1[p1] == s3[p3]:
                    memo[(p1, p2, p3)] = helper(p1 + 1, p2, p3 + 1)
                if s2[p2] == s3[p3]:
                    memo[(p1, p2, p3)] = memo[(p1, p2, p3)] or helper(p1, p2 + 1, p3 + 1)
            elif p1 < len(s1):
                if s1[p1] == s3[p3]:
                    memo[(p1, p2, p3)] = helper(p1 + 1, p2, p3 + 1)
            elif p2 < len(s2):
                if s2[p2] == s3[p3]:
                    memo[(p1, p2, p3)] = helper(p1, p2 + 1, p3 + 1)
            else:
                memo[(p1, p2, p3)] = False
            return memo[(p1, p2, p3)]
        
        return helper(0, 0, 0)
                
 