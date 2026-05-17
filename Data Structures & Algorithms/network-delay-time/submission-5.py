from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        visit = set()
        minHeap = [(0, k)]
        time = 0
        while minHeap:
            d, u = heappop(minHeap)
            if u in visit:
                continue
            visit.add(u)
            t = d
            for v, w in graph[u]:
                if v not in visit:
                    heappush(minHeap, (d + w, v))
        return t if len(visit) == n else -1 
        