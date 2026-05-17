from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        dist = [[float("inf")] * (k + 2) for _ in range(n)]

        dist[src][0] = 0

        minHeap = [(0, src, 0)]

        while minHeap:
            d, stop, count = heappop(minHeap)

            if d > dist[stop][count]:
                continue

            if stop == dst:
                return d

            for next_stop, w in graph[stop]:
                nd = d + w
                if count + 1 <= k + 1 and nd < dist[next_stop][count + 1]:
                    dist[next_stop][count + 1] = nd
                    heappush(minHeap, (nd, next_stop, count + 1))
        return -1
