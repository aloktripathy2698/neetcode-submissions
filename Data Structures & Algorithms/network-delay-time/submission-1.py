from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[k - 1] = 0

        for i in range(n - 1):
            for u, v, w in times:
                if dist[u - 1] + w < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + w
        res = max(dist)
        return res if res != float("inf") else -1