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
        mp = defaultdict(int)
        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1

        have = 0
        for i in sorted(mp):
            have += mp[i]
            if have == 2:
                return False
        
        return True
