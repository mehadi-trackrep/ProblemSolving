from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
	        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left) ## just swaping the right --> left & left --> right
            return root

if __name__ == "__main__":
    obj = Solution()
