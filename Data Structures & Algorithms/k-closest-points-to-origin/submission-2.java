class Solution {
    public int calculateDistance(int[] point){
        int x = point[0], y = point[1];
        return (x * x) + (y * y);
    }

    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> Integer.compare(calculateDistance(b), calculateDistance(a)));
        for(int[] point: points){
            maxHeap.offer(point);
            if (maxHeap.size() > k)
                maxHeap.poll();
        }

        int[][] res = new int[k][2];
        int idx = 0;
        while (maxHeap.size() > 0){
            res[idx++] = maxHeap.poll();
        }
        return res;
    }
}
