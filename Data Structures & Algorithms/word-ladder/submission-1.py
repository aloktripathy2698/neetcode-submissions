class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        q = deque([beginWord]) # ['bag']
        seen = set([beginWord]) # {'bat', 'bag'}
        level = 0 # 2
        while q:
            level += 1
            for _ in range(len(q)):
                word = q.popleft() # word = "bat"
                if word == endWord: # "bat" != 'sag'
                    return level
                for i in range(len(word)): # i = 0, word[i] = 'b'
                    for c in alphabets: # c = 'a'
                        newWord = word[:i] + c + word[i + 1:] # newWord = 'bag'
                        if newWord in wordSet and newWord not in seen:
                            seen.add(newWord)
                            q.append(newWord)
        return 0

"""
seen = {'hit', 'hot', 'dot', 'lot', 'dog', 'log', 'cog'}
level = 0
q = ['hit']
level = 1
q = ['hot']
level = 2
q = ['dot', 'lot']
level = 3
q = ['dog', 'log']
level = 4
q = ['cog']
level = 5

'hit' -> 'hot' -> 'dot' -> 'dog' -> 'cog'
"""