class KthLargest {
    private PriorityQueue<Integer> minHeap;
    private int K;

    public KthLargest(int k, int[] nums) {
        K = k;
        minHeap = new PriorityQueue<>();
        for(int num: nums){
            heapify(num);
        }
    }

    public void heapify(int num){
        minHeap.add(num);
        if(minHeap.size() > K)
            minHeap.poll();
    }
    
    public int add(int val) {
        heapify(val);
        return minHeap.peek();
    }
}
