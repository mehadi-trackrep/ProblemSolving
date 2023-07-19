from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ## considering that in this tree, there is no cycle!!
    ## and leaf node is indicated by NULL value.
    def DFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(
            1 + self.DFS(root.left), 
            1 + self.DFS(root.right)
        )

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root)
    
if __name__ == "__main__":
    obj = Solution()
    root = TreeNode(val=1, left=None, right=TreeNode(val=2))
    print(obj.maxDepth(root))
