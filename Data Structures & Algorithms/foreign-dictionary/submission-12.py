class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        indegree = {}

        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()
                    indegree[c] = 0

        n = len(words)
        count = len(graph)

        for i in range(1, n):
            w1, w2 = words[i - 1], words[i]
            n1, n2 = len(w1), len(w2)
            if n1 > n2 and w1[:n2] == w2:
                return ''
            for j in range(min(n1, n2)):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque()
        for node, degree in indegree.items():
            if degree == 0:
                q.append(node)

        res = []
        while q:
            node = q.popleft()
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
            res.append(node)

        return ''.join(res) if len(res) == count else ''

        

        