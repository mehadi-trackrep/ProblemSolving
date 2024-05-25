from typing import List

class Solution11:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        for i in range(m): # row - wise traverse
            for j in range(n): # column - wise traverse
                if i == 0 and j == 0:
                    res[i][j] = grid[i][j]
                if i > 0:
                    res[i][j] = min(res[i][j], res[i-1][j] + grid[i][j])
                if j > 0:
                    res[i][j] = min(res[i][j], res[i][j-1] + grid[i][j])
        
        return res[m-1][n-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(1, m): # row - wise traverse
            for j in range(1, n): # column - wise traverse
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        print(grid)
        return grid[m-1][n-1]

if __name__ == '__main__':
    obj = Solution()
    assert obj.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7