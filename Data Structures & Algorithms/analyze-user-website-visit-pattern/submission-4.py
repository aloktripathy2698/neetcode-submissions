from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        history = [(t, u, w) for t, u, w in zip(timestamp, username, website)]
        history.sort(key=lambda x: x[0])
        user_to_website = defaultdict(list)
        for t, u, w in history:
            user_to_website[u].append(w)
        pattern_to_score = defaultdict(int)

        largest_score = 0
        for user, websites in user_to_website.items():
            patterns = combinations(websites, 3)
            for pattern in patterns:
                pattern_to_score[pattern] += 1
                largest_score = max(pattern_to_score[pattern], largest_score)
        
        best_pattern = None
        for pattern, score in pattern_to_score.items():
            if score == largest_score:
                if best_pattern is None or pattern < best_pattern:
                    best_pattern = pattern
        return list(best_pattern)
            
