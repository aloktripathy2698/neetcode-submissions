class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))

        interval = []
        active = 0
        res = []

        events.sort(key=lambda x: (x[0], -x[1]))

        for event in events:
            if active == 0:
                start = event[0]
            active += event[1]
            if active == 0:
                interval = [start, event[0]]
                res.append(interval)
                interval = []

        return res

        