class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        tank = 0
        for i in range(len(gas)):
            if tank < 0:
                start = i
                tank = 0
            tank += (gas[i] - cost[i])
        return start