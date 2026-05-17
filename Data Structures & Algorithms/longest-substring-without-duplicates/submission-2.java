class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        HashMap<Character, Integer> mp = new HashMap<>();
        int maxLen = 0;

        for(int r = 0; r < s.length(); r++){
            char rightChar = s.charAt(r);
            mp.put(rightChar, mp.getOrDefault(rightChar, 0) + 1);

            while(mp.get(rightChar) > 1){
                char leftChar = s.charAt(l);
                mp.put(leftChar, mp.get(leftChar) - 1);
                l++;
            }

            maxLen = Math.max(maxLen, r - l + 1);
        }
        return maxLen;
    }
}
