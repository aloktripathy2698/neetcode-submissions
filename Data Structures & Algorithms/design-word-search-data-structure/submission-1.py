class Node:
    def __init__(self):
        self.children = {} 
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node() # [{d: [{a: [{y: [{}, True]}, False]}, False]}, False]

    def addWord(self, word: str) -> None: # day
        curr = self.root
        for c in word: # a
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.endOfWord = True
        
    def search(self, word: str) -> bool:
        # word = day, pos = 0
        def dfs(pos, node):
            curr = node # curr = {root}

            for i in range(pos, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.endOfWord

        return dfs(0, self.root)
        
