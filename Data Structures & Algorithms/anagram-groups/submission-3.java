class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> mp = new HashMap<>();
        for(String str: strs){
            int[] counts = new int[26];
            for(char c: str.toCharArray()){
                counts[c - 'a']++;
            }
            String key = Arrays.toString(counts);
            mp.putIfAbsent(key, new ArrayList<>());
            mp.get(key).add(str);
        }
        return new ArrayList<>(mp.values());
    }
}
