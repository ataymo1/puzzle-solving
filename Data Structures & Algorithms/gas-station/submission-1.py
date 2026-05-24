class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        cur_gas = 0
        index = 0
        lowest = 0

        if sum(gas) < sum(cost):
            return -1

        for i, pair in enumerate(zip(gas, cost)):
            gas_add, gas_cost = pair
            cur_gas += gas_add

            if gas_cost > cur_gas:
                index = i + 1
                lowest = min(lowest, cur_gas - gas_cost)
                cur_gas = 0
            else:
                cur_gas -= gas_cost

        index %= len(gas)
        
        return index % len(gas)
        