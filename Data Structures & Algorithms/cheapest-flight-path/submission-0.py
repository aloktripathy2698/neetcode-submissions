from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 2 ** 31 - 1
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        dist = [[INF] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        minHeap = [(0, src, 0)]
        while minHeap:
            d, u, stops = heappop(minHeap)
            if dist[u][stops] < d:
                continue
            if u == dst and stops <= k + 1:
                return d
            for v, w in graph[u]:
                if stops + 1 <= k + 1 and d + w < dist[v][stops + 1]:
                    dist[v][stops + 1] = d + w
                    heappush(minHeap, (d + w, v, stops + 1))
        return -1
