class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'}': '{', ']': '[', ')': '('}
        stack = []
        for c in s:
            if not stack or c not in mp or mp[c] != stack[-1]:
                stack.append(c)
            else:
                stack.pop()
        return stack == []
            
        