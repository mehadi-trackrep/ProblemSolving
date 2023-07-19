class Solution:
    
    grid = [[]]

    def dfs(self, i, j, r, c) -> None: ## it will go to all of it's connected adjacent cells and make them '0' (zero)
        if (i >= r or j >= c) or (i<0 or j<0):
            return
        if self.grid[i][j] == '0':
            return
        self.grid[i][j] = '0'
        self.dfs(i, j+1, r, c) # right side
        self.dfs(i+1, j, r, c) # down side
        self.dfs(i-1, j, r, c) # up side
        self.dfs(i, j-1, r, c) # left side


    def numIslands(self, grid: list[list[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        
        # visited = [[False]*c for _ in range(r)]
        # print(visited)

        self.grid = grid
        total_islands = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    total_islands += 1
                    self.dfs(i, j, r, c)
                    # print(grid)
        return total_islands

if __name__ == '__main__':
    obj = Solution()
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    grid1 = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]
    ]
    grid = [
        ["1","0","1","1","0","1","1"]
    ]
    print(obj.numIslands(grid=grid))