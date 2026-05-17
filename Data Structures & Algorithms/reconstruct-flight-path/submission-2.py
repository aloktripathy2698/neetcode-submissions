from heapq import heappush, heappop

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in tickets:
            heappush(graph[u], v)

        res = []

        def dfs(node):
            while graph[node]:
                dfs(heappop(graph[node]))
            res.append(node)

        dfs("JFK")
        return res[::-1]

        