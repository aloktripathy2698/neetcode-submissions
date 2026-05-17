class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        for i, c in enumerate(s):
            last[c] = i
        # last = {x: 3, y: 4, z: 7, b: 9, i: 10, s: 11, l: 12}

        res = [] # [5, 5, 1, 1]
        start = 0 # 12
        end = 0 #  12
        for i in range(len(s)):
            end = max(end,last[s[i]])
            if i == end: # 12 > 11
                res.append(end - start + 1)
                start = i + 1
        return res

        