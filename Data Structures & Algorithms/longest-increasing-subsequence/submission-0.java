class Solution {
    int[][] memo;

    public int helper(int i, int prevIdx, int[] nums){
        int n = nums.length;
        if(i == n)
            return 0;
        if(memo[i][prevIdx + 1] != -1)
            return memo[i][prevIdx + 1];
        if(prevIdx == -1 || nums[prevIdx] < nums[i]){
            memo[i][prevIdx + 1] = Math.max(1 + helper(i + 1, i, nums), helper(i + 1, prevIdx, nums));
        }
        else
            memo[i][prevIdx + 1] = helper(i + 1, prevIdx, nums);
        return memo[i][prevIdx + 1];

    }
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        memo = new int[n + 1][n + 1];
        for(int[] row: memo)
            Arrays.fill(row, -1);
        return helper(0, -1, nums);
    }
}
