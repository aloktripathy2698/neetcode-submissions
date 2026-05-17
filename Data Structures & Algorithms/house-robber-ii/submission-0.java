class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        return Math.max(
            linearRob(Arrays.copyOfRange(nums, 0, n - 1)),
            linearRob(Arrays.copyOfRange(nums, 1, n))
        );
    }

    private int linearRob(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n + 1];
        dp[1] = nums[0];
        for(int i = 2; i <= n; i++)
            dp[i] = Math.max(nums[i - 1] + dp[i - 2], dp[i - 1]);
        return dp[n];
    }
}