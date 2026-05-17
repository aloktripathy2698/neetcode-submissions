class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ''
        for c in s:
            if c.isalnum():
                r+= c.lower() if c.isupper() else c
        i,j=0,len(r)-1
        while i < j:
            if r[i] != r[j]:
                return False
            i+=1
            j-=1
        return True
        