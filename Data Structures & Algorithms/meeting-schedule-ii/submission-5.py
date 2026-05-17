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
40 -> -1
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = defaultdict(int)
        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1
        
        have = 0
        res = 0
        for i in sorted(mp):
            have += mp[i]
            res = max(have, res)
        return res
            
            
        