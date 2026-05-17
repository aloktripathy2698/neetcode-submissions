class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();

        for(String s: strs){
            String key = generateKey(s);
            if(!groups.containsKey(key))
                groups.put(key, new ArrayList<>());
            groups.get(key).add(s);
        }

        return new ArrayList<>(groups.values());
        
    }

    public String generateKey(String s){
        int[] count = new int[26];
        for(int i = 0; i < s.length(); i++)
            count[s.charAt(i) - 'a']++;
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < 26; i++){
            if(i > 0) sb.append(",");
            sb.append(count[i]);
        }
        return sb.toString();
    }
}
