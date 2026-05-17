class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()

        def dfs(r, c, idx):
            if idx == len(word) - 1:
                return True
            if board[r][c] != word[idx]:
                return False
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in seen and board[nr][nc] == word[idx + 1]:
                    if dfs(nr, nc, idx + 1):
                        return True
            seen.remove((r, c))
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
