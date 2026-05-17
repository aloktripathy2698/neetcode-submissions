class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        beginSet = {beginWord}
        endSet = {endWord}
        seen = {beginWord, endWord}
        level = 1
        while beginSet and endSet:
            if beginSet > endSet:
                beginSet, endSet = endSet, beginSet
            newSet = set()
            for word in beginSet:
                for i in range(len(word)):
                    for c in alphabets:
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in endSet:
                            return level + 1
                        if newWord in wordSet and newWord not in seen:
                            seen.add(newWord)
                            newSet.add(newWord)
            beginSet = newSet
            level += 1
        return 0
                        
"""
seen = {'cat', 'sag'}
beginSet = {'bag'}
endSet = {'sag'}
level = 2
newSet = {'sag'}


"""