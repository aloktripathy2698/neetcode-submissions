class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for c in string:
                pos = ord(c) - ord('a')
                arr[pos] += 1
            h = str(arr)
            groups[h].append(string)
        return groups.values()
        