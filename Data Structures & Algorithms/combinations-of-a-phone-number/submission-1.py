class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def solve(idx, temp):
            if idx == len(digits):
                res.append("".join(temp.copy()))
                return

            for c in mp[digits[idx]]:
                temp.append(c)
                solve(idx + 1, temp)
                temp.pop()

        solve(0, [])
        return res