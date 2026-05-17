from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        dist = [float("inf")] * n

        dist[k -1] = 0
        heap = [(0, k)]

        while heap:
            d, u = heappop(heap)
            if d > dist[u - 1]:
                continue
            
            for v, w in graph[u]:
                if dist[v - 1] > d + w:
                    dist[v - 1] = d + w
                    heappush(heap, (dist[v - 1], v))
        res = max(dist)
        return res if res != float('inf') else -1
        


        
