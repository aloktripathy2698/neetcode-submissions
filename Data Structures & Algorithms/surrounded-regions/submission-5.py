class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque()

        for r in range(rows):
            if board[r][0] == 'O':
                board[r][0] = 'T'
                q.append((r, 0))
            if board[r][cols - 1] == 'O':
                board[r][cols - 1] = 'T'
                q.append((r, cols - 1))

        for c in range(cols):
            if board[0][c] == 'O':
                board[0][c] = 'T'
                q.append((0, c))
            if board[rows - 1][c] == 'O':
                board[rows - 1][c] = 'T'
                q.append((rows - 1, c))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'T'
                    q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        

            

        
        