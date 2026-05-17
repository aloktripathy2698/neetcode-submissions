class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != '.':
                    if board[r][c] in rows[r]:
                        return False
                    else:
                        rows[r].add(board[r][c])
                    if board[r][c] in cols[c]:
                        return False
                    else:
                        cols[c].add(board[r][c])
                    if board[r][c] in squares[(r//3, c//3)]:
                        return False
                    else:
                        squares[(r//3, c//3)].add(board[r][c])
        return True

        