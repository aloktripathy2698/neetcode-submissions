class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int maxArea = 0;
        Stack<int[]> stack = new Stack<>();
        for(int i = 0; i < n; i++){
            int start = i;
            while(!stack.isEmpty() && stack.peek()[1] > heights[i]){
                int[] ele = stack.pop();
                int idx = ele[0], height = ele[1];
                maxArea = Math.max(maxArea, height * (i - idx));
                start = idx;
            }
            stack.push(new int[]{start, heights[i]});
        }
        for(int[] ele: stack){
            int idx = ele[0];
            int height = ele[1];
            maxArea = Math.max(maxArea, height * (n - idx));
        }
        return maxArea;
    }
}
