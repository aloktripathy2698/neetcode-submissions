"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))

        events.sort()

        res = 0
        active = 0
        for event in events:
            active += event[1]
            if active > res:
                res = active
        return res
