class Solution {

    public int calculate_distance(int[] p) {
        return p[0] * p[0] + p[1] * p[1];
    }

    public int[][] kClosest(int[][] points, int k) {

        PriorityQueue<int[]> max_heap = new PriorityQueue<>(
            (a, b) -> Integer.compare(calculate_distance(b), calculate_distance(a))
        );

        for (int[] point : points) {
            max_heap.offer(point);
            if (max_heap.size() > k) {
                max_heap.poll();
            }
        }

        int[][] res = new int[k][2];
        int i = 0;

        while (!max_heap.isEmpty()) {
            res[i++] = max_heap.poll();
        }

        return res;
    }
}
