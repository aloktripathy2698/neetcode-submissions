class Solution {
    public int[][] kClosest(int[][] points, int k) {
        
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (p1, p2) -> Integer.compare(distance(p2), distance(p1)));
        
        for(int[] point : points) {
            maxHeap.offer(point);
            if (maxHeap.size() > k)
                maxHeap.poll();
        }

        int[][] res = new int[k][2];
        int idx = 0;
        while (!maxHeap.isEmpty()) {
            int[] point = maxHeap.poll();
            res[idx++] = point;
        }

        return res;
    }

    private int distance(int[] p) {
        return p[0] * p[0] + p[1] * p[1];
    }
}
