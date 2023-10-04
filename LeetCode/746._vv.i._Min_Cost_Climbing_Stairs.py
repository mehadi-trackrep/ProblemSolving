from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # identify what is changing from subproblems to subproblems: 
        # n - step #n    dp(n) - min cost to get to step #n 
        mem = [-1 for _ in range(len(cost))]
        def dp(n):  
            # write down base cases
            if mem[n] != -1: return mem[n]
            if n < 2: return cost[n]
            # write recursive function based on what you can change (climb one or two steps)
            mem[n] = cost[n] + min(dp(n-1), dp(n-2))
            return mem[n]
		
		# since we want to know the min cost to get to the final step, we use the code below 
        length = len(cost) 
        return min(dp(length-1), dp(length-2))

if __name__ == '__main__':
    obj = Solution()
    assert obj.minCostClimbingStairs(cost=[10, 15, 20]) == 15
    assert obj.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6