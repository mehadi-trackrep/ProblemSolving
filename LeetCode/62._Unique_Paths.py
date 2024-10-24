class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [
            [0]*(n+1) for _ in range(m+1)
        ]
        
        dp[1][2] = 1
        dp[2][1] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] += (
                    dp[i][j-1] # from left side (rightwards)
                    + dp[i-1][j] # from up side (downwards)
                )
        
        return dp[m][n]
    
    
if __name__=="__main__":
    obj = Solution()
    print(obj.uniquePaths(3, 2))
    print(obj.uniquePaths(3, 7))