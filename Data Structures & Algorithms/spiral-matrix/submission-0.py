class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        leftBoundary = topBoundary = 0
        rightBoundary = cols - 1
        bottomBoundary = rows - 1
        direction = 'right'
        res = []
        while leftBoundary <= rightBoundary and topBoundary <= bottomBoundary:
            if direction == 'right':
                for c in range(leftBoundary, rightBoundary + 1):
                    res.append(matrix[topBoundary][c])
                topBoundary += 1
                direction = "down"
            elif direction == 'down':
                for r in range(topBoundary, bottomBoundary + 1):
                    res.append(matrix[r][rightBoundary])
                rightBoundary -= 1
                direction = 'left'
            elif direction == 'left':
                for c in range(rightBoundary, leftBoundary - 1, -1):
                    res.append(matrix[bottomBoundary][c])
                bottomBoundary -= 1
                direction = 'up'
            else:
                for r in range(bottomBoundary, topBoundary - 1, -1):
                    res.append(matrix[r][leftBoundary])
                leftBoundary += 1
                direction = 'right'
        return res



        