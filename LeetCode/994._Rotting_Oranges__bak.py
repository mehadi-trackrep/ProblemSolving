
class Solution:
    def __init__(self):
        # Direction vectors
        self.dRow = [ -1, 0, 1, 0]
        self.dCol = [ 0, 1, 0, -1]
        self.R = -1
        self.C = -1
        self.vis = [[]]
        self.grid = [[]]

    def isValid(self, row, col):

        # If cell lies out of bounds
        if (row < 0 or col < 0 or row >= self.R or col >= self.C):
            return False
        # If cell is already visited
        if (self.grid[row][col] in [0,2]): ## means visited!!
            return False
        # Otherwise
        return True

    # Function to perform the BFS traversal
    def BFS(self, row, col) -> int: ## return the level (/height)

        # Stores indices of the matrix cells
        q = []

        # Mark the starting cell as visited and push it into the queue
        q.append((row, col, 0)) ## 0 is the level
        self.grid[row][col] = 0 ## visited!
        mx_level = -1

        # Iterate while the queue is not empty
        while (len(q) > 0):
            cell = q.pop(0)
            x = cell[0]
            y = cell[1]
            level = cell[2]

            # print(self.grid[x][y], end = " ")

            ## Go to the adjacent cells
            for i in range(4):
                adjx = x + self.dRow[i]
                adjy = y + self.dCol[i]
                if (self.isValid(adjx, adjy)):
                    q.append((adjx, adjy, level+1))
                    self.grid[adjx][adjy] = 0 ## means visited
            mx_level = max(mx_level, level)
        return mx_level

    def orangesRotting(self, grid: list[list[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        self.R = r
        self.C = c
        self.grid = grid

        ## Do not using visited[]; instead of using grid, grid[0] means True otherwise False
        
        min_possible_time = 0

        for i in range(r):
            for j in range(c):
                if self.grid[i][j] == 2:
                    level = self.BFS(i, j)
                    # print("--> level: ", level)
                    min_possible_time = max(min_possible_time, level)
        for i in range(r):
            if 1 in grid[i]:
                return -1
        return min_possible_time

if __name__ == '__main__':
    obj = Solution()
    # grid = [[2,1,1],[1,1,0],[0,1,1]]
    # grid = [[2,1,1],[0,1,1],[1,0,1]]
    # grid = [[0,2]]
    # grid = [[1,2]]
    grid = [[0,2,2]]
    grid = [[2,1,1],[1,1,1],[0,1,2]]
    print(obj.orangesRotting(grid))