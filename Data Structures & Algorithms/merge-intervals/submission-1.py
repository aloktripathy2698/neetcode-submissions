class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prev = intervals[0]
        for interval in intervals[1:]:
            if prev[1] < interval[0]:
                res.append(prev)
                prev = interval
            elif interval[1] < prev[0]:
                res.append(interval)
            else:
                prev = [prev[0], max(prev[1], interval[1])]
        res.append(prev)
        return res

        