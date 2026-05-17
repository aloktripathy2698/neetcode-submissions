class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = collections.defaultdict(int)
        maxLen = 0
        for r in range(len(s)):
            window[s[r]] += 1
            while window[s[r]] > 1:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen

            


        