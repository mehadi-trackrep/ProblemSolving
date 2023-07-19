from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: ## we have to run 2 DFS!!
    # ans = -1
    def set_params(self):
        self.ans = -1
    def findHeightUsingDFSTraverse(self, root) -> int:
        if root == None:
            return 0
        left_node_height = self.findHeightUsingDFSTraverse(root.left)
        right_node_height = self.findHeightUsingDFSTraverse(root.right)
        self.ans = max(self.ans, left_node_height + right_node_height)
        return max(left_node_height, right_node_height) + 1
     
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.set_params()
        self.findHeightUsingDFSTraverse(root)
        return self.ans

if __name__ == "__main__":

    obj = Solution()
    
    TreeNode3 = TreeNode(3)
    TreeNode4 = TreeNode(4)
    TreeNode5 = TreeNode(5)

    TreeNode2 = TreeNode(2, TreeNode4, TreeNode5)
    TreeNode1 = TreeNode(1, TreeNode2, TreeNode3)

    root = TreeNode1

    print(obj.diameterOfBinaryTree(root))
