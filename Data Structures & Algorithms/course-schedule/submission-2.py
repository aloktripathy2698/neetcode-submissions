class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course: [] for course in range(numCourses)}
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        seen = set()

        def dfs(course):
            if course in seen:
                return False
            seen.add(course)
            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False
            seen.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True