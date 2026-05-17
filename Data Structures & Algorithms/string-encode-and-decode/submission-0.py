class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for string in strs:
            sub_string = f"{len(string)}#{string}"
            encoded_string.append(sub_string)
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j, jump = i, 0
            while s[j] != '#':
                jump = jump * 10 + int(s[j])
                j += 1
            i = j + jump + 1
            strs.append(s[j + 1 : i])
        return strs
            


