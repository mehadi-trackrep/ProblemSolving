from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_identical(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (
                self.is_identical(s.left, t.left) 
                    and 
                self.is_identical(s.right, t.right)
            )
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.is_identical(root, subRoot):
            return True
        return (
            self.isSubtree(root.left, subRoot) 
                or 
            self.isSubtree(root.right, subRoot)
        )


if __name__ == "__main__":
    ...