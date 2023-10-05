from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, so_far_sum):
            if not node: # last node
                return
            so_far_sum += node.val
            if not node.left and not node.right:
                if so_far_sum == targetSum:
                    return True
            return dfs(node.left, so_far_sum) or dfs(node.right, so_far_sum)
        return dfs(root, 0)
