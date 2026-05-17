class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = total_cost = 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
        
        if total_gas < total_cost:
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start = i + 1
                total = 0
        return start
        