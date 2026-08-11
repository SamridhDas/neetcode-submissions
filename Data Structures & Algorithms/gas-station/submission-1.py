class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res=0
        total_gas=sum(gas)
        total_cost=sum(cost)
        if total_gas<total_cost:
            return -1
        run=0
        for i in range(len(gas)):
            run+=gas[i]-cost[i]
            if run<0:
                res=i+1
                run=0
        return res
