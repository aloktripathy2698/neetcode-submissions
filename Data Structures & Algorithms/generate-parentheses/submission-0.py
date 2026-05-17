class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def isValid(s):
            count = 0
            for c in s:
                count = count + 1 if c == "(" else count - 1
                if count < 0: return False
            return count == 0

        def backtrack(curr):
            if len(curr) == 2 * n:
                if isValid(curr):
                    ans.append(curr)
                return
            
            backtrack(curr + "(")
            backtrack(curr + ")")

        backtrack('')
        return ans
                    
        