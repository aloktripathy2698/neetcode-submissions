class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)
        i = len(nums)
        res = []
        while i >= 0:
            while buckets[i]:
                res.append(buckets[i].pop())
                k -= 1
                if k == 0:
                    return res
            i -= 1
        