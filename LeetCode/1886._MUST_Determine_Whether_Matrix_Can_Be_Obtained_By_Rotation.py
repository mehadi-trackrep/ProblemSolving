from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """
            We know the rotation rule for square matrix using 2 steps.
                1. transpose
                2. reverse each row
            Hack: if we rotate a matrix repeteadly then after 90 rotation, then again 90 rotation which is in total
            180 rotation, again 90 rotation means 270 rotation, and if we again rotate it 4rth times then we
            get back the original matrix.
            
            So, we have to basically check up to `3 times` clockwise rotation.
        """
        if mat == target: return True
        
        n = len(mat)
        deg = 3
        
        while deg:

            #s1 transpose
            for i in range(n):
                for j in range(i, n):
                    temp = mat[i][j]
                    mat[i][j] = mat[j][i]
                    mat[j][i] = temp
            #s2 reverse
            for i in range(n):
                for j in range(n//2):
                    temp = mat[i][j]
                    mat[i][j] = mat[i][n-j-1]
                    mat[i][n-j-1] = temp
                # lj, rj = 0, n-1
                # while lj <= rj: # here, we have to use 2 pointers / go to the mid index in for loop
                #     temp = mat[i][lj]
                #     mat[i][lj] = mat[i][rj]
                #     mat[i][rj] = temp
                #     lj += 1
                #     rj -= 1
            
            if mat == target: return True

            deg -= 1
        
        return False
