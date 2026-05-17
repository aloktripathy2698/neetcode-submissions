class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int s = 0;
        int e = rows * cols - 1;
        while (s <= e){
            int m = s + (e - s) / 2;
            int r = m / cols;
            int c = m % cols;
            if (matrix[r][c] == target){
                return true;
            } else if (matrix[r][c] < target){
                s = m + 1;
            } else {
                e = m - 1;
            }
        }
        return false;
    }
}
