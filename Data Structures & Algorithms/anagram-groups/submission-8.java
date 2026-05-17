class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramGrps = new HashMap<>();

        for (String str : strs) {
            
            int[] counts = new int[26];
            
            for (char c : str.toCharArray()) {
                int idx = c - 'a';
                counts[idx]++;
            }

            String key = Arrays.toString(counts);

            if (!anagramGrps.containsKey(key))
                    anagramGrps.put(key, new ArrayList<>());
                
            anagramGrps.get(key).add(str);
        }

        List<List<String>> result = new ArrayList<>();

        anagramGrps.forEach((key, groups) -> {
            result.add(groups);
        });

        return result;
        
    }
}
