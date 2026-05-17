class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int n = points.length;
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(
                calculateDistance(b), calculateDistance(a)
            )
        );
        for (int[] point : points) {
            maxHeap.offer(point);
            if (maxHeap.size() > k)
                maxHeap.poll();
        }
        int[][] res = new int[maxHeap.size()][2];
        int idx = 0;
        while (!maxHeap.isEmpty())
            res[idx++] = maxHeap.poll();
        return res;
    }

    private int calculateDistance(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }
}
