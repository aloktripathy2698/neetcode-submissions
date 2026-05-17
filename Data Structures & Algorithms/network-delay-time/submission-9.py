from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)

        dist[k] = 0

        min_heap = [(0, k)]

        while min_heap:
            d, u = heappop(min_heap)

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(min_heap, (nd, v))

        res = max(dist[1:])
        return res if res != float("inf") else -1