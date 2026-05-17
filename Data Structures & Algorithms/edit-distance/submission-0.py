class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = defaultdict(int)
        def helper(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if i < len(word1) and j < len(word2):
                if word1[i] == word2[j]:
                    memo[(i, j)] = 1 + min(helper(i + 1, j + 1) - 1, helper(i + 1, j), helper(i, j + 1), helper(i + 1, j + 1))
                else:
                    memo[(i, j)] = 1 + min(helper(i + 1, j), helper(i, j + 1), helper(i + 1, j + 1))
            elif i < len(word1) and j == len(word2):
                memo[(i, j)] = 1 + helper(i + 1, j)
            elif i == len(word1) and j < len(word2):
                memo[(i, j)] = 1 + helper(i, j + 1)
            return memo[(i, j)]
        return helper(0, 0)
"""
insert -> i , j + 1
delete -> i + 1, j
replace -> i + 1, j + 1
same -> i + 1, j + 1
if word1[i] == word2[j]:
    return min(helper(i + 1, j + 1), helper(i, j + 1), helper(i + 1, j)
"""