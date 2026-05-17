from heapq import heapify, heappush, heappop

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        counts = Counter(hand) # {1: 2, 2: 2, 3: 2}
        nums = list(counts.keys())
        heapify(nums)
        while nums:
            min_ele = nums[0]
            for i in range(min_ele, min_ele + groupSize):
                if i not in counts:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    if i != nums[0]:
                        return False
                    heappop(nums)
        return True
            
            


