class Solution {
    public boolean isValidSudoku(char[][] board) {
        int rows = board.length;
        int cols = board[0].length;

        Map<Integer, Set<Character>> row_map = new HashMap<>();
        Map<Integer, Set<Character>> col_map = new HashMap<>();
        Map<String, Set<Character>> box_map = new HashMap<>();

        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                char ch = board[r][c];
                if(ch == '.') continue;
                String boxKey = (r/3) + "#" + (c/3);
                row_map.putIfAbsent(r, new HashSet<>());
                col_map.putIfAbsent(c, new HashSet<>());
                box_map.putIfAbsent(boxKey, new HashSet<>());
                if(
                    row_map.get(r).contains(ch)
                    || col_map.get(c).contains(ch)
                    || box_map.get(boxKey).contains(ch)
                )
                    return false;
                row_map.get(r).add(ch);
                col_map.get(c).add(ch);
                box_map.get(boxKey).add(ch);
            }
        }
        return true;
        
    }
}
/*
rowMap -> row: int: HashSet<int>, rowMap.get(r).contains(num) -> false
colMap -> col: int: HashSet<Int>, colMap.get(r).contains(num) -> false
boxMap -> String: '(r/3)#(c/3)'
*/