from heapq import heapify, heappush, heappop

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        mp = Counter(hand)
        minHeap = list(mp.keys())
        heapify(minHeap)

        while minHeap:
            min_ele = minHeap[0]
            for i in range(min_ele, min_ele + groupSize):
                if i not in mp:
                    return False
                mp[i] -= 1
                if mp[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heappop(minHeap)
        return True


        