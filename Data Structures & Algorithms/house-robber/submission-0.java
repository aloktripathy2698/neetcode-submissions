class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n + 1];
        dp[1] = nums[0];
        for(int i = 2; i <= n; i++)
            dp[i] = Math.max(nums[i - 1] + dp[i - 2], dp[i - 1]);
        return dp[n];
    }
}


/*
n = 0
amount = 0

n = 1
amount = nums[1]

n > 1
amount = max(nums[i] + solve(i + 2), solve(i + 1))
*/