class Solution {
    
    private static final int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public void dfs(char[][] grid, int r, int c){
        int rows = grid.length, cols = grid[0].length;
        grid[r][c] = '0';
        for(int[] dir: directions){
            int nr = r + dir[0], nc = c + dir[1];
            if((nr >= 0 && nr < rows) && (nc >= 0 && nc < cols) && grid[nr][nc] == '1')
                dfs(grid, nr, nc);
        }
    }

    public int numIslands(char[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int res = 0;
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                if(grid[r][c] == '1'){
                    res++;
                    dfs(grid, r, c);
                }
            }
        }
        return res;
    }
}
