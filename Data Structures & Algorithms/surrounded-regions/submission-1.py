class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    board[row][col] = 'T'
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if nr in range(rows) and nc in range(cols) and board[nr][nc] == 'O':
                            q.append((nr, nc))


        for c in range(cols):
            if board[0][c] == 'O':
                bfs(0,c)
            if board[rows - 1][c] == 'O':
                bfs(rows - 1, c)
        
        for r in range(rows):
            if board[r][0] == 'O':
                bfs(r,0)
            if board[r][cols - 1] == 'O':
                bfs(r, cols - 1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] ==  'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'