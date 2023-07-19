class Solution1:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix) # m
        c = len(matrix[0]) # n

        fill_0th_row, fill_0th_column = False, False

        ## V.V.I. ==> We will keep 1st row & 1st column as the markers/flags (like which rows & columns will be affected by a natural zero)

        ## Step 1 - set markers for inner matrix; 
                #   and 1st row, 1st col zero check
        for i in range(r):
            if matrix[i][0] == 0:
                fill_0th_column = True
            for j in range(c):
                if i == 0 and matrix[0][j] == 0: # check only for i=0 otherwise it will be affected by markers
                    fill_0th_row = True
                if i>=1 and j>=1: ## inner matrix
                    if matrix[i][j] == 0:
                        matrix[0][j] = 0 # a marker(/flag/checker)
                        matrix[i][0] = 0 # a marker
        
        print("--> fill_0th_row: ", fill_0th_row)
        print("--> fill_0th_column: ", fill_0th_column)
        print("--> matrix: {}\n".format(matrix))

        ## Step 2 - fill the marker wise columns (inner parts at first) & 0th row
            ## V.V.I. ==> we have to work at first for markers then followed by 0th row fillup!!
                    ## not like that at first 0th row then markers!! (it will create confusion for which are actully naturally)
        for j in range(1,c):
            if matrix[0][j] == 0:
                for i in range(r):
                    matrix[i][j] = 0
            if fill_0th_row:
                matrix[0][j] = 0
        if fill_0th_row:
                matrix[0][0] = 0

        ## Step 3 - fill the marker wise rows (inner parts at first) & 0th column
        for i in range(1,r):
            if matrix[i][0] == 0:
                for j in range(c):
                    matrix[i][j] = 0
            if fill_0th_column:
                matrix[i][0] = 0
        if fill_0th_column:
                matrix[0][0] = 0


        print("\n==> matrix: {}\n".format(matrix))

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix) # m
        c = len(matrix[0]) # n

        def mark_the_row_as_zeroes(i):
            for j in range(c):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = None

        def mark_the_column_as_zeroes(j):
            for i in range(r):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = None

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    mark_the_row_as_zeroes(i)
                    mark_the_column_as_zeroes(j)
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == None:
                    matrix[i][j] = 0

        print("==> matrix: ", matrix)


if __name__ == '__main__':
    obj = Solution()
    matrix = [[2,1,2,0], [3,4,5,2], [1,3,0,5], [1,3,1,5]]
    matrix = [[1,1,1], [1,0,1], [1,1,1]]
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    # matrix = [[1,0]]
    obj.setZeroes(matrix)