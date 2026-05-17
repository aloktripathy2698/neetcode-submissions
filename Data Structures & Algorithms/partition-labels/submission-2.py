class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i
        end, size, res = 0, 0, []
        for i in range(len(s)):
            size += 1
            end = max(end, last[s[i]])
            if i == end:
                res.append(size)
                size = 0
        return res
        

        