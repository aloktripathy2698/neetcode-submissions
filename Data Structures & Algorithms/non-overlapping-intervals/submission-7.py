class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev = intervals[0][1]
        res = 0
        for interval in intervals[1:]:
            if prev > interval[0]:
                res += 1
            else:
                prev = interval[1]
        return res