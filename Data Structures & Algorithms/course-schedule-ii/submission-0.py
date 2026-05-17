class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, indegree = defaultdict(list), [0] * numCourses
        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []
        while q:
            node = q.popleft()
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            res.append(node)
        return res if len(res) == numCourses else []