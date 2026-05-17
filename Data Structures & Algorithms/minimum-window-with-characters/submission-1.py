class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1, n2 = len(s), len(t)
        if n1 < n2:
            return ''

        ct, cs = {}, {}
        for c in t:
            ct[c] = ct.get(c, 0) + 1

        reqLen = n2
        left = 0
        start, end, minLen = -1, -1, float('inf')

        for right, c in enumerate(s):
            cs[c] = cs.get(c, 0) + 1

            if c in ct and cs[c] <= ct[c]:
                reqLen -= 1

            while reqLen == 0:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    start, end = left, right
                cs[s[left]] -= 1
                if s[left] in ct and cs[s[left]] < ct[s[left]]:
                    reqLen += 1
                left += 1
        return s[start: end + 1] if start != -1 else ""
        