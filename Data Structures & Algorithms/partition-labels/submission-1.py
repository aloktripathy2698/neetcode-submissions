class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        end = 0
        size = 0
        res = []
        for i in range(len(s)):
            size += 1
            end = max(end, last[s[i]])
            if i == end:
                res.append(size)
                size = 0
        return res








        