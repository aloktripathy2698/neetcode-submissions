class Solution {
    public int leastInterval(char[] tasks, int n) {
        
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char c : tasks)
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(b, a));

        freqMap.forEach((c, val) -> {
            maxHeap.offer(val);
        });

        int time = 0;

        while (!maxHeap.isEmpty()) {
            
            int currTime = 0;
            Deque<Integer> pending = new LinkedList<>();
            
            while (!maxHeap.isEmpty() && currTime <= n) {
                int freq = maxHeap.poll();
                freq--;
                if (freq != 0) 
                    pending.add(freq);
                currTime++;
            }

            while (!pending.isEmpty()) {
                maxHeap.offer(pending.pollFirst());
            }

            time += maxHeap.isEmpty() ? currTime : n + 1;
        }

        return time;

    }
}
