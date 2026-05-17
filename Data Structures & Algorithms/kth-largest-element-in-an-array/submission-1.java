class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        for(int num: nums){
            maxHeap.offer(num);
        }
        int i = 1;
        while(i < k){
            maxHeap.poll();
            i++;
        }
        return maxHeap.peek();
    }
}
