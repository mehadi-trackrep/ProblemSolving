# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    def bfs1(self, root): ## it's kinda of complex not exactly same as BFS traversing
        if not root:
            return
        
        d = {}
        d[0] = [root.val]
        level = 0
        queue = [(root, level)]

        while queue:
            val = queue.pop(0)
            node, level = val[0], val[1]
            l, r = None, None

            if node.left:
                queue.append((node.left, level + 1))
                l = node.left.val
            if node.right:
                queue.append((node.right, level + 1))
                r = node.right.val
            if l is not None or r is not None:
                level += 1
                if l is not None and r is not None:
                    if level in d:
                        d[level].extend([l, r])
                    else:
                        d[level] = [l, r]
                else:
                    if level in d:
                        d[level].append(l) if l is not None else d[level].append(r)
                    else:
                        d[level] = [l] if l is not None else [r]
        for each_item in d:
            self.ans.append(d[each_item])

    def bfs(self, root) -> List[List[int]]: ## it's easy and exactly same as BFS approach
        if not root: return []
        queue, res = [root], []
        
        while queue:
            cur_level_node_vals, sz = [], len(queue)
            for _ in range(sz):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level_node_vals.append(node.val)
            res.append(cur_level_node_vals)

        return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            Approach: BFS (level by level) using a queue
        """
        # self.ans = []
        # self.bfs1(root)
        # return [list(each_item) for each_item in self.ans]
        return self.bfs(root)

if __name__ == "__main__":
    obj = Solution()

    '''
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]
        Example 2:

        Input: root = [1]
        Output: [[1]]
        Example 3:

        Input: root = []
        Output: []

        [1,2,3,4,null,null,5]

        [-8,3,0,-8,null,null,null,null,-1,null,8]
    
    '''

    # print(obj.levelOrder(root))