class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1, c2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            i1 = ord(s1[i]) - ord('a')
            i2 = ord(s2[i]) - ord('a')
            c1[i1] += 1
            c2[i2] += 1

        if c1 == c2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            left = ord(s2[l]) - ord('a')
            right = ord(s2[r]) - ord('a')

            c2[left] -= 1
            c2[right] += 1

            if c1 == c2:
                return True

            l += 1
        
        return False
        