from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorder_traverse_DFS(self, root) -> str: ## here, 3 options (preorder, inorder, postorder)
        if not root:
            return 'null'
        return (
            str(root.val) + self.preorder_traverse_DFS(root.left) + self.preorder_traverse_DFS(root.right)
        )
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        preorder_string_from_p = self.preorder_traverse_DFS(p)
        preorder_string_from_q = self.preorder_traverse_DFS(q)
        if preorder_string_from_p == preorder_string_from_q:
            return True
        else:
            return False

if __name__ == "__main__":
    obj = Solution()
    # print(obj.isSameTree())
