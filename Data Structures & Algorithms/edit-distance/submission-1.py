class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = defaultdict(int)
        def helper(i, j):
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                memo[(i, j)] = helper(i + 1, j + 1)
            else:
                memo[(i, j)] = 1 + min(
                    helper(i + 1, j), 
                    helper(i, j + 1), 
                    helper(i + 1, j + 1)
                )
            
            return memo[(i, j)]
        return helper(0, 0)
