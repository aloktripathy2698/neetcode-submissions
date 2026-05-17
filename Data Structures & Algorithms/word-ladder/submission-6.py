class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        beginSet, endSet = {beginWord}, {endWord}
        seen = set([beginWord, endWord])

        level = 1
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            nextSet = set()
            for word in beginSet:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = word[:i] + c + word[i + 1:]
                        if nextWord in endSet:
                            return level + 1
                        elif nextWord in wordSet and nextWord not in seen:
                            nextSet.add(nextWord)
                            seen.add(nextWord)
            beginSet = nextSet
            level += 1
        return 0