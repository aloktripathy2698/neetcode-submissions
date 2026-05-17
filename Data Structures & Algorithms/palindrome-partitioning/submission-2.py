class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def solve(idx, partitions):
            if idx == len(s):
                ans.append(partitions.copy())
                return
            for i in range(idx, len(s)):
                if isPalindrome(idx, i):
                    partitions.append(s[idx: i + 1])
                    solve(i + 1, partitions)
                    partitions.pop()

        solve(0, [])
        return ans
