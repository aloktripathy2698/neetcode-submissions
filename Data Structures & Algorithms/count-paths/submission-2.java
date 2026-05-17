class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        for(int i = 0; i < m; i++)
            Arrays.fill(dp[i], -1);
        return helper(0, 0, m, n, dp);
    }

    public int helper(int r, int c, int rows, int cols, int[][] dp){
        if (r == rows || c == cols)
            return 0;
        if (r == rows - 1 && c == cols - 1)
            return 1;
        if(dp[r][c] != -1)
            return dp[r][c];
        dp[r][c] = helper(r + 1, c, rows, cols, dp) + helper(r, c + 1, rows, cols, dp);
        return dp[r][c];
    }
}
