class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0
        while q:
            node = q.popleft()
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
            count += 1
        return count == numCourses
