class Solution {

    private static final int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public boolean isValid(int rows, int cols, int r, int c){
        return r >= 0 && r < rows && c >= 0 && c < cols; 
    }

    public void bfs(char[][] grid, int r, int c){
        grid[r][c] = '0';
        int rows = grid.length;
        int cols = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{r, c});
        while(!q.isEmpty()){

            int[] position = q.poll();
            r = position[0]; 
            c = position[1];
            
            for(int[] dir: directions){
                int nr = r + dir[0];
                int nc = c + dir[1];

                if(isValid(rows, cols, nr, nc) && grid[nr][nc] == '1'){
                    grid[nr][nc] = '0';
                    q.offer(new int[]{nr, nc});
                }
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
                    bfs(grid, r, c);
                    numIslands++;
                }
            }
        }

        return numIslands;
        
    }
}
