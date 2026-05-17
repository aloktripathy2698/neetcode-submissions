class Solution {

    public boolean isValid(int rows, int cols, int r, int c){
        return r >= 0 && r < rows && c >= 0 && c < cols; 
    }

    public void dfs(char[][] grid, int r, int c){
        int rows = grid.length;
        int cols = grid[0].length;

        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for(int i = 0; i < 4; i++){
            int dr = directions[i][0];
            int dc = directions[i][1];

            int nr = r + dr;
            int nc = c + dc;
            if(isValid(rows, cols, nr, nc) && grid[nr][nc] == '1'){
                grid[nr][nc] = '0';
                dfs(grid, nr, nc);
            }
        }
    }
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        int numIslands = 0;
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                if(grid[r][c] == '1'){
                    grid[r][c] = '0';
                    dfs(grid, r, c);
                    numIslands++;
                }
            }
        }

        return numIslands;
        
    }
}
