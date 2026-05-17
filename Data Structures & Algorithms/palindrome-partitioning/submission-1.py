class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrack(pos, partitions):
            if pos >= len(s):
                ans.append(partitions.copy())
                return
            for j in range(pos, len(s)):
                if isPalindrome(pos, j):
                    partitions.append(s[pos:j + 1])
                    backtrack(j + 1, partitions)
                    partitions.pop()

        backtrack(0, [])
        return ans

        