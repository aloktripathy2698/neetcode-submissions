class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0][1]
        cnt = 0
        for interval in intervals[1:]:
            if prev <= interval[0]:
                prev = interval[1]
            else:
                cnt += 1
                prev = min(interval[1], prev)
        return cnt

        