from heapq import heapify, heappush, heappop

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        counts = {}
        for num in hand:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        minHeap = list(counts.keys())
        heapify(minHeap)

        while minHeap:
            min_ele = minHeap[0]
            for i in range(min_ele, min_ele + groupSize):
                if i not in counts:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heappop(minHeap)
        return True

        