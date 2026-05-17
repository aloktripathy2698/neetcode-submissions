class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        int n = nums.length;
        Deque<Integer>[] buckets = new LinkedList[n + 1];

        Map<Integer, Integer> counts = new HashMap<>();

        for (int num : nums)
            counts.put(num, counts.getOrDefault(num, 0) + 1);

        counts.forEach((num, freq) -> {
            if (buckets[freq] == null)
                buckets[freq] = new LinkedList<>();
            buckets[freq].offer(num);
        });

        int i = n;
        int[] res = new int[k];
        int index = 0;
        while (i >= 0) {
            while ((buckets[i] != null) && !buckets[i].isEmpty()) {
                res[index++] = buckets[i].poll();
                k--;
                if (k == 0)
                    return res;
            }
            i--;
        }

        return new int[] {};

    }
}
