class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue(Collections.reverseOrder());
        for(int stone: stones)
            heap.add(stone);
        while(heap.size() > 1){
            int x = heap.poll();
            int y = heap.poll();
            int z = Math.abs(x - y);
            heap.add(z);
        }
        return heap.isEmpty() ? 0 : heap.peek();
    }
}
