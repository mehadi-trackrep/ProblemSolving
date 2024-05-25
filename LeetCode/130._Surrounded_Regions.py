from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r, c = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c: # if out of index
                return
            if board[i][j] == "X" or board[i][j] == "F": # if already visited or a 'X'
                return
            
            board[i][j] = "F" # false means shouldn't be flipped
            
            dfs(i+1, j) # down
            dfs(i-1, j) # up
            dfs(i, j+1) # right
            dfs(i, j-1) # left
            
        # print("--> board: ", board)
        for i in range(r):
            for j in range(c):
                # invoke dfs only for boundary cells to mark all of the adjacent lands 
                # to reach out from the boundaries
                if (i == 0 or i == r-1) or (j == 0 or j == c-1):
                    dfs(i, j)
        # print("==> board: ", board)
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "F":
                    board[i][j] = "O"
                else:
                    ...
        # print("#   board: ", board)

obj = Solution()
obj.solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])