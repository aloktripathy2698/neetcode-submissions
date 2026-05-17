from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        minHeap = [(0, k)]

        while minHeap:
            d, u = heappop(minHeap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heappush(minHeap, (d + w, v))
        
        res = max(dist[1:])
        return res if res != float('inf') else -1

        