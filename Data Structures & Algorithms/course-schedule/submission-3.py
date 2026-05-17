class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course: [] for course in range(numCourses)}
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
            indegree[prerequisite] += 1

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        count = 0
        while q:
            course = q.popleft()
            for prerequisite in graph[course]:
                indegree[prerequisite] -= 1
                if indegree[prerequisite] == 0:
                    q.append(prerequisite)
            count += 1
        return count == numCourses


        