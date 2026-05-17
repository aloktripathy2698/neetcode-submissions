class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] dp = new int[n + 1];
        for(int i = 2; i < n + 1; i++)
            dp[i] = Math.min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2]);
        return dp[n];
    }
}

/*
n = 0
0

n = 1
cost[0]

n = 2
cost

cost[i] + min(solve(i + 1), solve(i + 2))
*/