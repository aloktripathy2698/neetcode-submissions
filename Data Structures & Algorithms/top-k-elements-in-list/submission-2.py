class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        heap = []
        for num, count in counts.items():
            if len(heap) == k:
                heapq.heappushpop(heap, (count, num))
            else:
                heapq.heappush(heap, (count, num))
        return [num for count, num in heap]

            