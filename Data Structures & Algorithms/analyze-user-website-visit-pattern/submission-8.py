class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = list(zip(timestamp, username, website))
        visits.sort(key=lambda x: x[0])

        user_to_web = defaultdict(list)
        for t, u, w in visits:
            user_to_web[u].append(w)

        def combinations(websites, size):
            patterns = set()

            def solve(idx, temp):
                if len(temp) == size:
                    patterns.add(tuple(temp.copy()))
                    return
                for i in range(idx, len(websites)):
                    temp.append(websites[i])
                    solve(i + 1, temp)
                    temp.pop()

            solve(0, [])
            return patterns

        pattern_count = defaultdict(int)
        max_score = 0
        top_pattern = None
        for user, websites in user_to_web.items():
            patterns = combinations(websites, 3)
            for pattern in patterns:
                pattern_count[pattern] += 1
                if pattern_count[pattern] > max_score:
                    max_score = pattern_count[pattern]
                    top_pattern = pattern
                elif pattern_count[pattern] == max_score and top_pattern > pattern:
                    top_pattern = pattern
        return list(top_pattern)

