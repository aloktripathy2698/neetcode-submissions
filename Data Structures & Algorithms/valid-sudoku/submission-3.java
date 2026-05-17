class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<String, Set<Character>> boxes = new HashMap<>();

        for(int r = 0; r < 9; r++){
            for(int c = 0; c < 9; c++){
                if(board[r][c] == '.')
                    continue;
                
                if(rows.containsKey(r) && rows.get(r).contains(board[r][c])){
                    return false;
                } else {
                    if(!rows.containsKey(r)){
                        rows.put(r, new HashSet<>());
                    }
                    rows.get(r).add(board[r][c]);
                }

                if(cols.containsKey(c) && cols.get(c).contains(board[r][c])){
                    return false;
                } else {
                    if(!cols.containsKey(c)){
                        cols.put(c, new HashSet<>());
                    }
                    cols.get(c).add(board[r][c]);
                }

                String boxKey = (r/3) + "," + (c/3);
                if(boxes.containsKey(boxKey) && boxes.get(boxKey).contains(board[r][c])){
                    return false;
                } else {
                    if(!boxes.containsKey(boxKey)){
                        boxes.put(boxKey, new HashSet<>());
                    }
                    boxes.get(boxKey).add(board[r][c]);
                }
            }
        }
        
        return true;
    }
}
