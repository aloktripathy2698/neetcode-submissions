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
        minHeap = []
        for interval in intervals:
            if minHeap and minHeap[0] <= interval.start:
                heappop(minHeap)
            heappush(minHeap, interval.end)
        return len(minHeap)

        