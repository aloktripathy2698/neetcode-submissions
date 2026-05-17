class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        counts1 = [0] * 26
        counts2 = [0] * 26

        for i in range(n1):
            i1, i2 = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            counts1[i1] += 1
            counts2[i2] += 1

        for i in range(n1, n2):
            if counts1 == counts2:
                return True
            
            add_at = ord(s2[i]) - ord('a')
            remove_from = ord(s2[i - n1]) - ord('a')
            counts2[add_at] += 1
            counts2[remove_from] -= 1

        return counts1 == counts2
        