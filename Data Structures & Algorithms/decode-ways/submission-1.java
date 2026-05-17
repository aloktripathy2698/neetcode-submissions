class Solution {
    int[] dp;

    public int helper(int i, String s){
        int n = s.length();
        
        if(i == n)
            return 1;

        if(dp[i] != -1)
            return dp[i];

        if(s.charAt(i) == '0')
            return 0;

        int result = helper(i + 1, s);
        if (i < n - 1){
            if(s.charAt(i) == '1' || (s.charAt(i) == '2' && s.charAt(i + 1) <= '6'))
                result += helper(i + 2, s);
        }
        dp[i] = result;
        return dp[i];
    }

    public int numDecodings(String s) {
        int n = s.length();
        dp = new int[n + 1];
        Arrays.fill(dp, -1);
        return helper(0, s);
    }
}