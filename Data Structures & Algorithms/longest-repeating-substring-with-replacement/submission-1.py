class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = [0] * 26
        maxLen = 0
        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            counts[idx] += 1
            while (r - l + 1) - max(counts) > k:
                pos = ord(s[l]) - ord('A')
                counts[pos] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
            
        