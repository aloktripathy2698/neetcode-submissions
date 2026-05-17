class Solution {
    public int trap(int[] height) {
        int n = height.length;

        int[] maxLeft = new int[n];
        int[] maxRight = new int[n];

        for(int i = 1; i < n; i++)
            maxLeft[i] = Math.max(height[i-1], maxLeft[i - 1]);

        for(int i = n - 2; i >= 0; i--)
            maxRight[i] = Math.max(height[i + 1], maxRight[i + 1]);

        int maxArea = 0;
        for(int i = 0; i < n; i++) {
            int currArea = Math.min(maxLeft[i], maxRight[i]) - height[i];
            maxArea += currArea <= 0 ? 0 : currArea;
        }

        return maxArea;
        
    }
}
