class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n1 = s1.length(), n2 = s2.length();

        if(n1 > n2)
            return false;

        int[] s1_count = new int[26];
        int[] s2_count = new int[26];

        for(int r = 0; r < n1; r++){
            s1_count[s1.charAt(r) - 'a']++;
            s2_count[s2.charAt(r) - 'a']++;
        }

        int matches = 0;
        for(int i = 0; i < 26; i++){
            if(s1_count[i] == s2_count[i])
                matches++;
        }

        
        int l = 0;
        for(int r = n1; r < n2; r++){
            if(matches == 26)
                return true;

            int index = s2.charAt(r) - 'a';
            s2_count[index]++;

            if(s1_count[index] == s2_count[index])
                matches++;
            else if(s1_count[index] + 1 == s2_count[index])
                matches--;

            index = s2.charAt(l) - 'a';
            s2_count[index]--;

            if(s1_count[index] == s2_count[index])
                matches++;
            else if(s1_count[index] == s2_count[index] + 1)
                matches--;
            l++;
        }
        return matches == 26;
    }
}
