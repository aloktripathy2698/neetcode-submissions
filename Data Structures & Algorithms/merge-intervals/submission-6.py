class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = intervals[0]
        res = []
        for interval in intervals[1:]:
            if prev[1] >= interval[0]:
                prev[1] = max(prev[1], interval[1])
            else:
                res.append(prev)
                prev = interval
        res.append(prev)
        return res 