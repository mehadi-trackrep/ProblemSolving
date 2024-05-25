from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c: # if out of index
                return
            if grid[i][j] == 0 or grid[i][j] == -1: # if already visited or a sea cell
                return
            
            grid[i][j] = -1
            
            dfs(i+1, j) # down
            dfs(i-1, j) # up
            dfs(i, j+1) # right
            dfs(i, j-1) # left
            
            
        for i in range(r):
            for j in range(c):
                # invoke dfs only for boundary cells to mark all of the adjacent lands 
                # to reach out from the boundaries
                if (i == 0 or i == r-1) or (j == 0 or j == c-1):
                    dfs(i, j)
        
        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    ans += 1
                    
        return ans