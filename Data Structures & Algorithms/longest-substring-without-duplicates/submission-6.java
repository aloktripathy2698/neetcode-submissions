class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> count = new HashMap<>();
        int maxLen = 0;
        int l = 0;
        for(int r = 0; r < s.length(); r++){
            char c = s.charAt(r);
            count.put(c, count.getOrDefault(c, 0) + 1);
            while(count.get(c) > 1){
                char prevC = s.charAt(l);
                count.put(prevC, count.get(prevC) - 1);
                l++;
            }
            maxLen = Math.max(maxLen, r - l + 1);
        }
        return maxLen;
    }
}
