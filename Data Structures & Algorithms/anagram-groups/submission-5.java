class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        int n = strs.length;
        if(n == 0)
            return new ArrayList<>();
        Map<String, List<String>> mp = new HashMap<>();
        for(String str: strs){
            String key = helper(str);
            if(!mp.containsKey(key))
                mp.put(key, new ArrayList<>());
            mp.get(key).add(str);
        }
        List<List<String>> result = new ArrayList<>();
        for(Map.Entry<String, List<String>> entry: mp.entrySet()){
            result.add(entry.getValue());
        }
        return result;
    }

    public String helper(String s){
        int[] counts = new int[26];
        for(char c: s.toCharArray())
            counts[c - 'a']++;
        StringBuilder sb = new StringBuilder();
        for(int count: counts)
            sb.append(count).append('#');
        return sb.toString();
    }
}

/*
strs = [] -> []
strs.length() == 1 -> return [[strs]];

mp = string(count): list<strings>
count = 26 elements
*/