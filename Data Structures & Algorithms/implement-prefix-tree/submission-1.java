class TrieNode{
    private HashMap<Character, TrieNode> children;
    private boolean endOfWord;

    public TrieNode(){
        this.children = new HashMap<>();
        this.endOfWord = false; 
    }
}

class PrefixTree {

    private TrieNode root;

    public PrefixTree() {
        this.root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode curr = this.root;
        for(int i = 0; i < word.length(); i++){
            char c = word.charAt(i);
            if(!curr.children.containsKey(c)){
                curr.children.put(c, new TrieNode());
            }
            curr = curr.children.get(c);
        }
        curr.endOfWord = true;
    }

    public boolean search(String word) {
        TrieNode curr = root;
        for(int i = 0; i < word.length(); i++){
            char c = word.charAt(i);
            if(!curr.children.containsKey(c)){
                return false;
            }
            curr = curr.children.get(c);
        }
        return curr.endOfWord;
    }

    public boolean startsWith(String prefix) {
        TrieNode curr = root;
        for(int i = 0; i < prefix.length(); i++){
            char c = prefix.charAt(i);
            if(!curr.children.containsKey(c)){
                return false;
            }
            curr = curr.children.get(c);
        }
        return true;
    }
}
