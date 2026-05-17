class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return True
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            if matrix[r][0] <= target <= matrix[r][cols-1]:
                return binary_search(matrix[r])
        return False
        