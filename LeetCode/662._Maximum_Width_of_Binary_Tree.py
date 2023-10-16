# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def bfs() -> int:
            max_width = 0
            if not root:
                return max_width
            queue = [(root, 0)] # format: tuple => (node, id)
            while queue: # level wise traverse..
                temp_queue = []
                min_id, max_id = float('inf'), float('-inf')

                while queue: # visit all nodes in a level..
                    t = queue.pop(0)
                    node = t[0]
                    node_id = t[1]

                    if node.left:
                        min_id = min(min_id, node_id*2 + 1)
                        max_id = max(max_id, node_id*2 + 1)
                        temp_queue.append((node.left, node_id*2 + 1))
                    if node.right:
                        min_id = min(min_id, node_id*2 + 2)
                        max_id = max(max_id, node_id*2 + 2)
                        temp_queue.append((node.right, node_id*2 + 2))

                max_width = max(max_width, max_id - min_id + 1 if max_id != float('-inf') else 1)
                queue = temp_queue
            return max_width
        
        return bfs()

if __name__ == "__main__":
    obj = Solution()
    # print(obj.widthOfBinaryTree(root = [1,3,2,5,3,None,9]))
    # print(obj.widthOfBinaryTree(root = [1])) -> 1