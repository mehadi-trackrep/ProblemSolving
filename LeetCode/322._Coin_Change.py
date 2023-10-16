class Solution:
    
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        dp = [float('inf') for _ in range(amount+1)]
        sz = len(coins)
        dp[0] = 0
        for i in range(1,amount+1):
            for j in range(sz): # iterate the ways/paths for finding the min way for i
                if coins[j] <= i: # as we have to find the minimum n(coins) needed for the target amount.
                        # so, as we have infinite supply of coins, we can use the same coin multiple times.
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == '__main__':
    obj = Solution()
    assert obj.coinChange([1,2,5], 11) == 3