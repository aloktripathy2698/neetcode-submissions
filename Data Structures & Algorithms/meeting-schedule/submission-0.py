"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key=lambda x: x.end)
        prev = intervals[0].end # 8
        for interval in intervals[1:]:
            if prev > interval.start: # 8 > 8 No
                return False
            prev = interval.end
        return True

# [(0,8),(8,10)]
