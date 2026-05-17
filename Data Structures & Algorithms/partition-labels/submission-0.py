class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        end = -1
        size = 0
        res = []
        for i in range(len(s)):
            if i > end:
                size = 1
                end = last[s[i]]
                if i == end:
                    res.append(size)
            elif i < end:
                size += 1
                end = max(end, last[s[i]])
            else:
                res.append(size + 1)
        return res








        