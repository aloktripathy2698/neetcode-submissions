class Solution {
    private int[][] memo;
    private static final int INF = (int) 1e9;

    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        memo = new int[n + 1][amount + 1];
        for(int i = 0; i <= n; i++)
            Arrays.fill(memo[i], -1);
        int res = helper(0, amount, coins);
        return res == INF ? -1 : res;
    }

    public int helper(int i, int amount, int[] coins){
        int n = coins.length;
        if(i >= n || amount < 0)
            return INF;
        if(amount == 0)
            return 0;
        if(memo[i][amount] != -1)
            return memo[i][amount];
        memo[i][amount] = Math.min(1 + helper(i, amount - coins[i], coins), helper(i + 1, amount, coins));
        return memo[i][amount];
    }
}


/*
if coins.len = 0
    return 0
if amount = 0
    return 0
helper(i, amount) = min(1 + helper(i, amount - coins[i]), helper(i + 1, amount))
*/
