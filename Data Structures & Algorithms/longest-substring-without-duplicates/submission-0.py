class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, ans, window = 0, 0, collections.defaultdict(int)
        for r in range(len(s)):
            window[s[r]] += 1
            while window[s[r]] > 1:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
             
        