class Solution {
    private final int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int res = 0;
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                if(grid[r][c] == '1'){
                    res++;
                    bfs(r, c, grid);
                }
            }
        }
        return res;
    }

    public boolean inBounds(int r, int c, int rows, int cols){
        return (r >= 0 && r < rows) && (c >= 0 && c < cols);
    }

    public void bfs(int r, int c, char[][] grid){
        int rows = grid.length;
        int cols = grid[0].length;
        grid[r][c] = '0';
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{r, c});
        while(!q.isEmpty()){
            int[] land = q.poll();
            r = land[0];
            c = land[1];
            for(int[] dir: directions){
                int nr = r + dir[0], nc = c + dir[1];
                if(inBounds(nr, nc, rows, cols) && grid[nr][nc] == '1'){
                    grid[nr][nc] = '0';
                    q.offer(new int[]{nr, nc});
                }
            }
        }
    }

}
