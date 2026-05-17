class Solution {
    public int helper(int i, int n, Map<Integer, Integer> memo){
        if(i > n)
            return 0;
        if(i == n)
            return 1;
        if(memo.containsKey(i))
            return memo.get(i);
        memo.put(i, memo.getOrDefault(i, helper(i + 1, n, memo) + helper(i + 2, n, memo)));
        return memo.get(i);
    }

    public int climbStairs(int n) {
        Map<Integer, Integer> memo = new HashMap<>();
        return helper(0, n, memo);
    }
}
