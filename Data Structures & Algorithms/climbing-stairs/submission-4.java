class Solution {
    int[] memo;
    public int helper(int i, int n){
        if(i > n)
            return 0;
        if(i == n)
            return 1;
        if(memo[i] != -1)
            return memo[i];
        memo[i] = helper(i + 1, n) + helper(i + 2, n);
        return memo[i];
    }

    public int climbStairs(int n) {
        memo = new int[n + 1];
        Arrays.fill(memo, -1);
        return helper(0, n);
    }
}
