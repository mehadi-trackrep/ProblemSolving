from typing import Optional

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int: # with splitting & without splitting in each node
        max_sum = float('-inf')
        
        '''
            Intuition:-
                For each node will split the path, meaning go to left & right subtrees.
                But when we will return then we have to ensure a single path.
                So, return current_node_val + max(left_val, right_val) # select max path
                And in between will will just calculate the max_path value & finally return the max_path out of 
                the dfs() inner function.
            N.B. In a state - if we have negative values from left and right subtrees then
                we don't want to add the paths to the current node and return
        '''
        
        def dfs(root):
            if not root: # Null
                return 0
            
            nonlocal max_sum

            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)
            
            max_sum = max(max_sum, root.val + left_max + right_max)
            
            return root.val + max(left_max, right_max)
        
        dfs(root)

        return max_sum

if __name__ == '__main__':
    obj = Solution()
    # assert obj.maxPathSum([1,2,3]) == 6