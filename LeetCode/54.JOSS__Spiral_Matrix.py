from typing import List

class Solution:
    def isInsideBoundary_and_notVisited(self, x, y) -> bool:
        if x>=0 and x<self.m and y>=0 and y<self.n and self.matrix[x][y] != None: return True
        return False
        
    def traverse_matrix_in_spiral_order(self, x, y) -> list:
        """
            As we will start from the topmost left position - (0,0), so the traversing priority will be like
            
            1) go right direction till the boundary / visited already   [y++]
            2) similarly, down direction                                [x++]
            3) left                                                     [y--]
            4) up                                                       [x--]
            
            if all the 4 steps failed then break/return
        """
        output = []
        total_elements = self.m * self.n
        traversing_direction_flag = 1 # 1 -> right, 2 -> down, 3 -> left, 4 -> up

        while len(output) < total_elements:
            
            output.append(self.matrix[x][y])
            self.matrix[x][y] = None # visited
            
            print(f"--> enter: (x,y): ({x},{y})")
            
            if traversing_direction_flag == 1:
                if self.isInsideBoundary_and_notVisited(x, y+1): #s1: right
                    y += 1
                else:
                    traversing_direction_flag = 2
                    x += 1
            elif traversing_direction_flag == 2:
                if self.isInsideBoundary_and_notVisited(x+1, y): #s2: down
                    x += 1
                else:
                    traversing_direction_flag = 3
                    y -= 1
            elif traversing_direction_flag == 3:
                if self.isInsideBoundary_and_notVisited(x, y-1): #s3: left
                    y -= 1
                else:
                    traversing_direction_flag = 4
                    x -= 1
            else:
                if self.isInsideBoundary_and_notVisited(x-1, y): #s4: up
                    x -= 1
                else:
                    traversing_direction_flag = 1
                    y += 1

            print(f"==> exc: (x,y): ({x},{y})\n")
        
        return output
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        self.m, self.n, self.matrix = m, n, matrix
        
        return self.traverse_matrix_in_spiral_order(0, 0)
    
if __name__=="__main__":
    obj = Solution()
    # print(obj.spiralOrder(matrix=[[1,2,3],[4,5,6],[7,8,9]]))
    
    print(obj.spiralOrder(matrix=[[2,5],[8,4],[0,-1]]))
    
    print(obj.spiralOrder(matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]))
    
    