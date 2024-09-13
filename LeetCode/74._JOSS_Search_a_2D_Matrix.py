from typing import List

class Solution:
    """
        Ref: https://leetcode.com/problems/search-a-2d-matrix/solutions/1895837/c-binary-search-tree-explained-with-img/
        V.V.I. & Tricky!!
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        cur_row, cur_col = 0, cols - 1 # as we have to start from right side!
        
        # based on the above condition, in this iterative approach, 
        # the `cur_row` might remain in the same position or might be increased (towards bottom)
        # and `cur_col` might remain in the same position or might be decrease (towards left)
        
        while cur_row < rows and cur_col >= 0:
            if matrix[cur_row][cur_col] == target: return True
            elif matrix[cur_row][cur_col] < target: cur_row += 1
            else: cur_col -= 1
        
        return False