class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> window = new HashMap<>();
        
        int left = 0;
        int maxLen = 0;

        for(int right = 0; right < s.length(); right++) {
            char rightChar = s.charAt(right);
            window.put(rightChar, window.getOrDefault(rightChar, 0) + 1);

            while (window.get(rightChar) > 1) {
                char leftChar = s.charAt(left);
                window.put(leftChar, window.get(leftChar) - 1);
                left++;
            }

            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}
