from typing import Optional

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(root):
            if not root: return 0
            nonlocal max_sum
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            print("--> left: {}, right: {}".format(left, right))
            max_sum = max(max_sum, max(left, right)) # by taking any one of the child subtree
            max_sum = max(max_sum, root.val + left + right) # by taking all with root
            max_sum = max(max_sum, max(root.val + left, root.val + right)) # by taking one child with root
            print("==> max_sum: {}".format(max_sum))
            return max_sum
        
        dfs(root)

        return max_sum

if __name__ == '__main__':
    obj = Solution()
    # assert obj.maxPathSum([1,2,3]) == 6