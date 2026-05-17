class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
            if i == len(s) - 1 or j == -1:
                return True
            if i in range(len(s)) and j in range(len(s)) and s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
