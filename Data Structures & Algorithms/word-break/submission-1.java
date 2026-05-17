class Solution {
    Boolean[] dp;

    public boolean helper(int i, String s, Set<String> wordSet){
        int n = s.length();
        if(i == n)
            return true;
        if(dp[i] != null)
            return dp[i];
        for(int j = i + 1; j <= n; j++){
            if(wordSet.contains(s.substring(i, j)) && helper(j, s, wordSet)){
                dp[i] = true;
                return dp[i];
            }
        }
        dp[i] = false;
        return dp[i];
    }

    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        dp = new Boolean[n + 1];
        Set<String> wordSet = new HashSet<>(wordDict);
        return helper(0, s, wordSet);
    }
}
