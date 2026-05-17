class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        memo = {}

        def helper(i, j):
            if i == 0 or j == 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i - 1] == text2[j - 1]:
                memo[(i, j)] = 1 + helper(i - 1, j - 1)
            else:
                memo[(i, j)] = max(helper(i - 1, j), helper(i, j - 1))
            return memo[(i, j)]

        return helper(n, m)
        

'''
n1 = 0, n2 = 0 -> 0
if text1[i] == text2[j]:
    helper(i, j) = 1 + helper(i - 1, j - 1)
else:
    helper(i, j) = max(helper(i - 1, j), helper(i, j - 1))
'''