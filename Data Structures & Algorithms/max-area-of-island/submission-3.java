class Solution {
    
    private static final int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int maxAreaOfIsland(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;

        int maxArea = 0;
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                if(grid[r][c] == 1)
                    maxArea = Math.max(maxArea, dfs(grid, r, c));
            }
        }
        return maxArea;
    }

    public int dfs(int[][] grid, int r, int c){
        int rows = grid.length, cols = grid[0].length;
        grid[r][c] = 0;
        int area = 1;
        for(int[] dir: directions){
            int nr = r + dir[0], nc = c + dir[1];
            if(
                (nr >= 0 && nr < rows)
                && (nc >= 0 && nc < cols)
                && (grid[nr][nc] == 1)
            )
                area += dfs(grid, nr, nc);
        }
        return area;
    }
}
