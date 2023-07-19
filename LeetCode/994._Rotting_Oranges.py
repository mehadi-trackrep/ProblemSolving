
class Solution:
    def __init__(self):
        self.dRow = [ -1, 0, 1, 0]
        self.dCol = [ 0, 1, 0, -1]
        self.rows = -1
        self.cols = -1
        self.total_fresh_oranges = 0
        self.rotten_oranges = []

    def isValid(self, grid, x, y):
        # If cell lies out of bounds
        if (x < 0 or y < 0 or x >= self.rows or y >= self.cols):
            return False
        # If cell is already visited
        if (grid[x][y] in [0,2]): ## means visited!!
            return False
        # Otherwise
        return True

    def BFS_traverse(self, grid): ## multi source BFS traversing simultaneously
        queue = self.rotten_oranges
        time = 0
        total_affected_fresh_oranges = 0
        temp_queue = []

        while queue or temp_queue:
            while queue:
                cell = queue.pop(0)
                x = cell[0]
                y = cell[1]
                ## Go to the adjacent cells
                for i in range(4):
                    adjx = x + self.dRow[i]
                    adjy = y + self.dCol[i]
                    if (self.isValid(grid, adjx, adjy)):
                        temp_queue.append((adjx, adjy))
                        total_affected_fresh_oranges += 1
                        grid[adjx][adjy] = 0 ## means visited
            if temp_queue:
                time += 1
            queue = temp_queue
            temp_queue = []

        return time if total_affected_fresh_oranges == self.total_fresh_oranges else -1

    def orangesRotting(self, grid: list[list[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 2:
                    self.rotten_oranges.append((i, j))
                elif grid[i][j] == 1:
                    self.total_fresh_oranges += 1
        return self.BFS_traverse(grid)


if __name__ == '__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    # grid = [[2,1,1],[0,1,1],[1,0,1]]
    # grid = [[0,2]]
    # grid = [[1,2]]
    # grid = [[0,2,2]]
    # grid = [[2,1,1],[1,1,1],[0,1,2]]
    grid = [[2,0,0,2], [1,1,1,1], [0,0,1,1]]
    obj = Solution()
    print(obj.orangesRotting(grid))