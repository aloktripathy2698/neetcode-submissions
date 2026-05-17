class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(root, i):
            curr = root
            for i in range(i, len(word)):
                if word[i] == '.':
                    for c in curr.children:
                        if dfs(curr.children[c], i + 1):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.endOfWord

        return dfs(self.root, 0)
            
        
