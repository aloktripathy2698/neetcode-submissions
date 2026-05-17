class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for c in s:
            if (c not in mp) or (not stack) or (stack[-1] != mp[c]):
                stack.append(c)
            else:
                stack.pop()
        return stack == []
