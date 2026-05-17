class KthLargest {
    private int k;
    private int[] nums;
    private PriorityQueue<Integer> minHeap;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.nums = nums;
        this.minHeap = new PriorityQueue<>();
        for(int num : nums) {
            heapify(num);
        }
    }
    
    public int add(int val) {
        heapify(val);
        return minHeap.peek();
    }

    private void heapify(int val) {
        minHeap.offer(val);
        if (minHeap.size() > k)
            minHeap.poll();
    }
}
