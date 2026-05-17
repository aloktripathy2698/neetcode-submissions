from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = [float("inf")] * n
        dist[k - 1] = 0
        minHeap = [(0, k)]

        while minHeap:
            d, u = heappop(minHeap)
            if dist[u - 1] < d:
                continue
            for v, w in graph[u]:
                new_d = d + w
                if new_d < dist[v - 1]:
                    dist[v - 1] = new_d
                    heappush(minHeap, (new_d, v))

        res = max(dist)
        return res if res != float('inf') else -1
