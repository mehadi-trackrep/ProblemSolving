from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Initialize the total cost to 0
        total_cost = 0
        # Sort the costs list in ascending order based on the difference
        # between the costs of sending someone to city A vs city B
        costs.sort(key = lambda x : x[0] - x[1])
        # Get the length of the costs list
        cost_length = len(costs)
        # For each pair of cities, add the cost of sending one person to city A and the other person to city B to the total cost
        for i in range(cost_length//2):
            total_cost = total_cost + costs[i][0] + costs[cost_length-i-1][1];
        # Return the total cost
        return total_cost
