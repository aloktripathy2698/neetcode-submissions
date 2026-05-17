class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(r, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in range(rows):
            s, e = 0, cols - 1
            while s < e:
                matrix[r][s], matrix[r][e] = matrix[r][e], matrix[r][s]
                s += 1
                e -= 1
        

"""
[
    [ 21,  16,  11,  6,  1],
    [ 22,  17,  12,  7, 2],
    [23, 18, 13, 8, 3],
    [24, 19, 14, 9, 4],
    [25, 20, 15, 10, 5]
]

[
    [21, 16, 11,  6,  1],
    [22, 17, 12,  7,  2],
    [23, 18, 13,  8,  3],
    [24, 19, 14,  9,  4],
    [25, 20, 15, 10,  5]
]
"""