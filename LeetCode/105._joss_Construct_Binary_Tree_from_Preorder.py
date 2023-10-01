# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
            We will find the root node from left subtree & right subtree
            by passing the sliced preorder & inorder list recursively.

            Suppose:
                preorder = ["3",9,5, 20,15,7]
                inorder = [9,5,"3", 15,20,7]

            Then:
                root = 3
                left subtree = [9,5] 
                right subtree = [15,20,7]
                So, here the preorder list = [9,5] & inorder list = [9,5]
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        root_pos = inorder.index(preorder[0]) # Find the root node in inorder list
        root.left = self.buildTree(preorder[1:root_pos+1], inorder[:root_pos])
        root.right = self.buildTree(preorder[root_pos+1:], inorder[root_pos+1:])
        return root

if __name__ == "__main__":
    obj = Solution()
    root = obj.buildTree([3,9,20,15,7], [9,3,15,20,7])
    print(root.val)