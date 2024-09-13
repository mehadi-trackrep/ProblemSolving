from typing import List

class Solution:
    
    """

        V.V.I.__MUST resource: 
            https://leetcode.com/problems/valid-sudoku/solutions/5272799/video-keep-number-we-found-and-find-duplicate/

    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #1st rule:
        for i in range(9):
            freq = [0] * 10
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    if freq[int(val)] == 1:
                        return False
                    else:
                        freq[int(val)] = 1

        #2nd rule:
        for j in range(9):
            freq = [0] * 10
            for i in range(9):
                val = board[i][j]
                if val != ".":
                    if freq[int(val)] == 1:
                        return False
                    else:
                        freq[int(val)] = 1
                
        # 3rd rule:
        it = 0
        while it < 9:
            
            # print(f"--> it: {it}")
            loop_cnt = 0
            
            while loop_cnt < 3:
                
                j_start = loop_cnt * 3
                freq = [0] * 10
                
                for i in range(it, it+3): # it -> starting indices i, j
                    for j in range(j_start, j_start+3):
                        print(f"==> (i,j): ({i}, {j})")
                        val = board[i][j]
                        if val != ".":
                            if freq[int(val)] == 1:
                                return False
                            else:
                                freq[int(val)] = 1
                loop_cnt += 1
                # print("\n++++++++++++++++++++++\n")
            it += 3
        
        return True

if __name__=="__main__":
    obj = Solution()
    print(obj.isValidSudoku(
        # board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        board=[[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    ))