class Solution {
    Boolean[][] dp;

    public int sum(int[] nums){
        int total = 0;
        for(int i = 0; i < nums.length; i++)
            total += nums[i];
        return total;
    }

    public boolean subset_sum(int i, int[] nums, int target){
        int n = nums.length;
        if(target == 0)
            return true;
        if(i == n || target < 0)
            return false;
        if(dp[i][target] != null)
            return dp[i][target];
        dp[i][target] = subset_sum(i + 1, nums, target - nums[i]) || subset_sum(i + 1, nums, target);
        return dp[i][target];
    }

    public boolean canPartition(int[] nums) {
        int n = nums.length;
        int total = sum(nums);

        if(total % 2 != 0)
            return false;

        int target = (int) total / 2;

        dp = new Boolean[n + 1][target + 1];

        return subset_sum(0, nums, target);
    }
}
