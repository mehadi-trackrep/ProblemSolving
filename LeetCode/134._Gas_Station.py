from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Check if it is possible to complete the journey based on total gas and cost.
        if sum(cost) > sum(gas):  
            return -1             

        # Initialize variables for tracking total gas and starting index.
        current_gas, starting_index = 0, 0

        # Iterate over all gas stations in the list.
        for i in range(len(gas)):  
        
            # Update current gas level by adding gas and subtracting cost at current station.
            current_gas = current_gas + (gas[i] - cost[i])
            
            # If the current gas level is negative, reset it to zero and update the starting index.
            if current_gas < 0:
                current_gas = 0
                starting_index = i + 1

        # Return starting index of gas station that allows journey to be completed.
        return starting_index