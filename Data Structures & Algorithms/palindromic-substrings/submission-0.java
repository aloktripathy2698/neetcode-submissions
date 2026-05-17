class Solution {
    public int palindrome(String s, int l, int r){
        int n = s.length();
        int count = 0;
        while(l >= 0 && r < n && s.charAt(l) == s.charAt(r)){
            count++;
            l--;
            r++;
        }
        return count;
    }

    public int countSubstrings(String s) {
        int n = s.length();
        int count = 0;
        for(int i = 0; i < n; i++)
            count += palindrome(s, i, i) + palindrome(s, i, i + 1);
        return count;
    }
}
