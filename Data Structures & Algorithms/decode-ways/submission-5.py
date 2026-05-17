class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        cache = defaultdict(int)

        def helper(i):
            if i > len(s):
                return 0
            if i == len(s):
                return 1
            if i in cache:
                return cache[i]
            if int(s[i]) != 0:
                if int(s[i: i + 2]) <= 26:  
                    cache[i] = helper(i + 1) + helper(i + 2)
                else:
                    cache[i] = helper(i + 1)
            return cache[i]

        return helper(0)