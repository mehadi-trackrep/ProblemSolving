# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:

    def dfs(self, root):
        if self.is_found:
            return
        if not root:
            return
        
        if root.left:
            self.dfs(root.left)
        
        self.k -= 1
        if self.k == 0:
            self.is_found = True
            self.ans = root.val
            return
        
        if root.right:
            self.dfs(root.right)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
            in order traversal - but at first go to the last node in left section and 
            then back one by one decreasing k-=1 when k==0 that node is the smallest one!
        """
        self.ans, self.is_found, self.k = -1, False, k
        self.dfs(root)
        return self.ans

if __name__ == "__main__":
    obj = Solution()
    '''
        Input: root = [3,1,4,null,2], k = 1
        Output: 1

        Input: root = [5,3,6,2,4,null,null,1], k = 3
        Output: 3
    '''

    n1 = TreeNode(2)
    n2 = TreeNode(4)
    n3 = TreeNode(1, right=n1)
    n4 = TreeNode(3, left=n3, right=n2)
    root = n4
    # assert obj.kthSmallest(root, 1) == 1
    print(obj.kthSmallest(root, 1))

    n1 = TreeNode(1)
    n2 = TreeNode(4)
    n3 = TreeNode(6)
    n4 = TreeNode(2, left=n1)
    n5 = TreeNode(3, left=n4, right=n2)
    n6 = TreeNode(5, left=n5, right=n3)
    root = n6
    # assert obj.kthSmallest(root, 3) == 3
    print(obj.kthSmallest(root, 3))
