class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: [] for word in words for c in word}
        indegree = {c: 0 for word in words for c in word}

        n = len(words)

        for i in range(n - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].append(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque()
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)

        res = []
        while q:
            c = q.popleft()
            for next_c in graph[c]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    q.append(next_c)
            res.append(c)
        return "".join(res) if len(res) == len(indegree) else ""
