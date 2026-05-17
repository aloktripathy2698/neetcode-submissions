class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, ans, counts = 0, 0, collections.defaultdict(int)
        for r in range(len(s)):
            counts[s[r]] += 1
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans


        