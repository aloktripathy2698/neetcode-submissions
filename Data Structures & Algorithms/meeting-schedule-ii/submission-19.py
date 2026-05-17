"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []
        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heappop(min_heap)
            heappush(min_heap, interval.end)
        return len(min_heap)