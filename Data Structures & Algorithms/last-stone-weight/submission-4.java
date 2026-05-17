class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        for(int stoneWeight : stones) {
            maxHeap.offer(stoneWeight);
        }

        while (maxHeap.size() > 1) {
            int x = maxHeap.poll();
            int y = maxHeap.poll();
            if (x == y) continue;
            int newWeight = Math.abs(x - y);
            maxHeap.offer(newWeight);
        }

        return maxHeap.size() == 0 ? 0 : maxHeap.peek();
    }
}
