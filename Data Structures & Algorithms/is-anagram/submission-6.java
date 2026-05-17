class Solution {
    public boolean isAnagram(String s, String t) {
        int n1 = s.length();
        int n2 = t.length();

        if (n1 != n2)
            return false;

        int[] counts1 = new int[26];
        int[] counts2 = new int[26];

        for (int i = 0; i < n1; i++) {
            int idx1 = s.charAt(i) - 'a';
            int idx2 = t.charAt(i) - 'a';
            counts1[idx1]++;
            counts2[idx2]++;
        }

        return Arrays.equals(counts1, counts2);


    }
}
