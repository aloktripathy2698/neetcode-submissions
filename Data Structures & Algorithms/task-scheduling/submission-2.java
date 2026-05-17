class Solution {
    public int leastInterval(char[] tasks, int n) {
        HashMap<Character, Integer> counts = new HashMap<>();
        for(char c: tasks)
            counts.put(c, counts.getOrDefault(c, 0) + 1);
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for(Map.Entry<Character, Integer> entry: counts.entrySet())
            maxHeap.offer(entry.getValue());
        int time = 0;
        while(!maxHeap.isEmpty()){
            Deque<Integer> dq = new ArrayDeque<>();
            int cnt = 0;
            while(!maxHeap.isEmpty() && cnt <= n){
                int freq = maxHeap.poll();
                freq--;
                if(freq > 0)
                    dq.offer(freq);
                cnt++;
            }
            if(!dq.isEmpty())
                time += n + 1;
            else
                time += cnt;
            while(!dq.isEmpty())
                maxHeap.offer(dq.pollFirst());
        }
        return time;
    }
}
