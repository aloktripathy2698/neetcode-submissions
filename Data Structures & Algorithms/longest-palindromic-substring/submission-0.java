class Solution {
    int resIdx;
    int resLen;

    public void validPalindrome(String s, int l, int r){
        int n = s.length();
        while(l >= 0 && r < n && s.charAt(l) == s.charAt(r)){
            if(r - l + 1 > resLen){
                resLen = r - l + 1;
                resIdx = l;
            }
            l--;
            r++;
        }
    }

    public String longestPalindrome(String s) {
        resLen = 0;
        int n = s.length();
        for(int i = 0; i < n; i++){
            validPalindrome(s, i, i);
            validPalindrome(s, i, i + 1);
        }
        return s.substring(resIdx, resIdx + resLen);
    }
}
