class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # same as - 1143. Longest Common Subsequence
        # Approach: LCS tabulation cause Memoization we have to go kinda deep levels that's why it gives TLE
        text1 = s
        text2 = s[::-1]
        m = len(text1) # row
        n = len(text2) # col
        dp = [[0]*(n+1) for _ in range(m+1)] # m+1 by n+1 matrix
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]