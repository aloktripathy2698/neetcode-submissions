class Solution {
    private int[][] dp;

    public int helper(int i, int j){
        if(i == 0 && j == 0)
            return 1;
        if(i < 0 || j < 0)
            return 0;
        if(dp[i][j] != -1)
            return dp[i][j];
        dp[i][j] = helper(i - 1, j) + helper(i, j - 1);
        return dp[i][j];
    }

    public int uniquePaths(int m, int n) {
        dp = new int[m][n];
        for(int i = 0; i < m; i++)
            Arrays.fill(dp[i], -1);
        return helper(m - 1, n - 1);
    }
}

/*
if n == 0 or n == 1:
    return n
helper(i, j) = helper(i - 1, j) + helper(i, j - 1)
*/