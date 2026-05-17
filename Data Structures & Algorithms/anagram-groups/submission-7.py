class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def get_hash(s):
            counts = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                counts[idx] += 1
            return "#".join([str(c) for c in counts])

        groups = {}

        for s in strs:
            key = get_hash(s)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())

        