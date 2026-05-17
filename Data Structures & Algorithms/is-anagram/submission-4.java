class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length())
            return false;

        Map<Character, Integer> s1 = new HashMap<>();
        Map<Character, Integer> s2 = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            s1.put(s.charAt(i), s1.getOrDefault(s.charAt(i), 0) + 1);
            s2.put(t.charAt(i), s2.getOrDefault(t.charAt(i), 0) + 1);
        }

        return s1.equals(s2);

    }
}
