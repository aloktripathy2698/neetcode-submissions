class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        for(int stone: stones){
            maxHeap.add(-stone);
        }

        while(maxHeap.size() > 1){
            int x = -maxHeap.remove();
            int y = -maxHeap.remove();
            y = Math.abs(x - y);
            maxHeap.add(-y);
        }

        return maxHeap.isEmpty() ? 0: -maxHeap.peek();
        
    }
}
