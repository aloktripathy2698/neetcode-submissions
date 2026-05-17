from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        minHeap = [(0, k)]

        while minHeap:
            d, u = heappop(minHeap)

            if d < dist[u]:
                continue

            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(minHeap, (nd, v))
        
        res = max(dist[1:])
        return res if res != float('inf') else -1

