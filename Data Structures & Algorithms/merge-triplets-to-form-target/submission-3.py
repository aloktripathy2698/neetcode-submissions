class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for triplet in triplets:
            if target[0] < triplet[0] or target[1] < triplet[1] or target[2] < triplet[2]:
                continue
            for i in range(3):
                if triplet[i] == target[i]:
                    good.add(i)
        return len(good) == 3