# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode: OR,
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ...
        print("--> ", root.val)
        if root is None:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            print("==> ",root.val)
            return root

if __name__=='__main__':
    obj = Solution()

    leaf1 = TreeNode(4)
    leaf2 = TreeNode(10)
    leaf3 = TreeNode(14)
    leaf4 = TreeNode(22)

    interm1 = TreeNode(12)
    interm1.left = leaf2
    interm1.right = leaf3

    interm2 = TreeNode(8)
    interm2.left = leaf1
    interm2.right = interm1

    root = TreeNode(20)
    root.left = interm2
    root.right = leaf4

    '''
                20
              /  \
            8    22
            /  \
            4     12
                /   \
                10   14
    '''
    
    # obj.lowestCommonAncestor(root, leaf1, leaf2)
    # obj.lowestCommonAncestor(root, leaf2, leaf3)
    obj.lowestCommonAncestor(root, interm1, leaf4)
