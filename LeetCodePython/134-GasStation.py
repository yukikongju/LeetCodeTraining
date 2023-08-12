#  https://leetcode.com/problems/gas-station/description/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # solution: Greedy -> 

        # --- 
        differences = [g - c for g, c in zip(gas, cost)]

        # --- greedy
        start_index, total_gas, remaining_gas = 0, 0, 0
        for i in range(len(gas)):
            total_gas += differences[i]
            remaining_gas += differences[i]
            if remaining_gas < 0:
                start_index = i + 1
                remaining_gas = 0
        
        return start_index if total_gas >= 0 else -1

