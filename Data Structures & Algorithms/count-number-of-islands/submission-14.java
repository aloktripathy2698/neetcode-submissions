class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        boolean[][] seen = new boolean[rows][cols];

        int numIslands = 0;

        for(int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1' && seen[r][c] == false) {
                    bfs(grid, seen, r, c);
                    numIslands++;
                }
            }
        }

        return numIslands;
        
    }

    private void bfs(char[][] grid, boolean[][] seen, int r, int c) {
        int rows = grid.length, cols = grid[0].length;
        int[][] directions = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};

        seen[r][c] = true;
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {r, c});

        while (!q.isEmpty()) {
            int[] coords = q.pollFirst();
            r = coords[0];
            c = coords[1];

            for (int[] dir : directions) {
                int nr = r + dir[0], nc = c + dir[1];

                if (
                    nr >= 0 && nr < rows
                    && nc >= 0 && nc < cols
                    && grid[nr][nc] == '1'
                    && seen[nr][nc] == false
                ) {
                    q.offer(new int[] {nr, nc});
                    seen[nr][nc] = true;
                }
            }
        }


    }

}
