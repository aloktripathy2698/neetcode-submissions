class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, i, seen):
            if i == len(word) - 1:
                return True
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and i + 1 < len(word) and word[i + 1] == board[nr][nc] and (nr, nc) not in seen:
                    if dfs(nr, nc, i + 1, seen):
                        return True
            seen.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True
        return False
        