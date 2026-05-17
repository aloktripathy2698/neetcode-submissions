class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // Max-Heap: stores indices, sorted by distance descending
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(calculateDistance(b, points), calculateDistance(a, points))
        );

        for (int i = 0; i < points.length; i++) { // Corrected .length
            maxHeap.offer(i);
            if (maxHeap.size() > k) {
                maxHeap.poll(); // Remove the largest distance to keep the 'k' smallest
            }
        }

        int[][] res = new int[k][2];
        int idx = 0;
        while (!maxHeap.isEmpty()) {
            res[idx++] = points[maxHeap.poll()];
        }
        return res;
    }

    private int calculateDistance(int idx, int[][] points) {
        // We don't need Math.sqrt for comparison; squared distance is enough
        return points[idx][0] * points[idx][0] + points[idx][1] * points[idx][1];
    }
}