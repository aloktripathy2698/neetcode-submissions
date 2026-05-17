class Solution {
    int[][] dp;

    public int helper(int i, int[] coins, int amount){
        int n = coins.length;
        if(amount == 0)
            return 0;
        if(amount < 0 || i == n)
            return 10001;
        if(dp[i][amount] != -1)
            return dp[i][amount];
        dp[i][amount] = Math.min(1 + helper(i, coins, amount - coins[i]), helper(i + 1, coins, amount));
        return dp[i][amount];
    }

    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        dp = new int[n + 1][amount + 1];
        for (int[] row : dp) 
            Arrays.fill(row, -1);
        int result = helper(0, coins, amount);
        return result > amount ? -1 : result;
    }
}