"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

0 -> 1
5 -> 1
10 -> -1
15 -> 1
20 -> -1
30 -> -1
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        prev = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < prev:
                return False
            prev = interval.end
        return True