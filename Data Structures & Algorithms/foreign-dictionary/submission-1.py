class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        indegree = {}
        for w in words:
            for c in w:
                if c not in graph:
                    graph[c] = set()
                    indegree[c] = 0

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque([c for c in indegree if indegree[c] == 0])

        res = []

        while q:
            c = q.popleft()
            res.append(c)
            for neigbor in graph[c]:
                indegree[neigbor] -= 1
                if indegree[neigbor] == 0:
                    q.append(neigbor)
        
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)