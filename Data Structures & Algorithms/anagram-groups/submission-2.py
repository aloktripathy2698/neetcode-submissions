class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                counts[idx] += 1
            counts = str(counts)
            if counts not in mp:
                mp[counts] = []
            mp[counts].append(s)
        return list(mp.values())

        