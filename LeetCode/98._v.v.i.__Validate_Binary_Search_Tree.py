# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    """
        Approach: 
            a node will be in a valid position if it's in between 
                lower & upper bound.
            Case 1:
                if we go to the left node then the upper bound will be it's immediate parent node
                and the lower bound will be the same as it's parent node's lower bound (-ve inf or something).
            Case 2:
                if we go to the right node then the lower bound will be it's immediate parent node
                and the upper bound will be the same as it's parent node's upper bound (+ve inf or something).
    """
    def dfs(self, root: Optional[TreeNode], lower: int, upper: int) -> bool:
        if root is None:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        return self.dfs(root.left, lower, root.val) and self.dfs(root.right, root.val, upper)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    obj = Solution()
    
    n1 = TreeNode(2) # root
    n2 = TreeNode(1)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    assert obj.isValidBST(n1) == True
    
    n1 = TreeNode(3) # root
    n2 = TreeNode(1)
    n3 = TreeNode(6)
    n4 = TreeNode(2)
    n5 = TreeNode(7)
    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5
    assert obj.isValidBST(n1) == False
