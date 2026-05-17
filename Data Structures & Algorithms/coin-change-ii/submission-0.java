class Solution {
    int[][] memo;

    public int change(int amount, int[] coins) {
        int n = coins.length;
        memo = new int[n + 1][amount + 1];
        for(int[] row: memo)
            Arrays.fill(row, -1);
        return helper(0, amount, coins);
    }

    public int helper(int i, int amount, int[] coins){
        int n = coins.length;
        if(i >= n || amount < 0)
            return 0;
        if(amount == 0)
            return 1;
        if(memo[i][amount] != -1)
            return memo[i][amount];
        memo[i][amount] = helper(i, amount - coins[i], coins) + helper(i + 1, amount, coins);
        return memo[i][amount];
    }
}
