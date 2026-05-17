class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(curr, open, close):
            if len(curr) == 2 * n:
                ans.append(curr)
                return
            
            if open < n:
                backtrack(curr + "(", open + 1, close)
            if close < open:
                backtrack(curr + ")", open, close + 1)

        backtrack('', 0, 0)
        return ans
                    
        