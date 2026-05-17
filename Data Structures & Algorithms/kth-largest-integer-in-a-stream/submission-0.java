class KthLargest {

    private int heapSize;
    private PriorityQueue<Integer> minHeap;

    public KthLargest(int k, int[] nums) {
        minHeap = new PriorityQueue<>();
        heapSize = k;

        for(int num: nums){
            add(num);
        }
    }
    
    public int add(int val) {
        minHeap.add(val);
        if(minHeap.size() > heapSize){
            minHeap.remove();
        }
        return minHeap.peek();
    }
}
