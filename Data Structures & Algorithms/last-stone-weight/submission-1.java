class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for(int stone: stones){
            maxHeap.offer(stone);
        }

        while(maxHeap.size() > 1){
            int x = maxHeap.poll();
            int y = maxHeap.poll();
            maxHeap.offer(x - y);
        }

        return maxHeap.isEmpty() ? 0: maxHeap.peek();
        
    }
}
