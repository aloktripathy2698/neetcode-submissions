class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rowMap = new HashMap<>();
        Map<Integer, Set<Character>> colMap = new HashMap<>();
        Map<String, Set<Character>> boxMap = new HashMap<>();

        for(int r = 0; r < 9; r++){
            for(int c = 0; c < 9; c++){
                if(board[r][c] == '.')
                    continue;

                String boxKey = (r/3) + "," + (c/3);
                
                if(
                    rowMap.computeIfAbsent(r, k -> new HashSet<>()).contains(board[r][c])
                    || colMap.computeIfAbsent(c, k -> new HashSet<>()).contains(board[r][c])
                    || boxMap.computeIfAbsent(boxKey, k -> new HashSet<>()).contains(board[r][c])
                ) {
                    return false;
                }

                rowMap.get(r).add(board[r][c]);
                colMap.get(c).add(board[r][c]);
                boxMap.get(boxKey).add(board[r][c]);
            }
        }
        return true;
    }
}
