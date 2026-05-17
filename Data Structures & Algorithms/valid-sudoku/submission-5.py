class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        boxMap = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rowMap[r]:
                    return False
                if board[r][c] in colMap[c]:
                    return False
                if board[r][c] in boxMap[(r//3, c // 3)]:
                    return False
                rowMap[r].add(board[r][c])
                colMap[c].add(board[r][c])
                boxMap[(r//3, c//3)].add(board[r][c])
        return True
        