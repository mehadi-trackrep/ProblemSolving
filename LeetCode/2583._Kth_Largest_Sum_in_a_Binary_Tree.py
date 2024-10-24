from typing import Optional
from heapq import heappush, heappop

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        q = [] # queue
        q.append((root, 1)) # storing pair of (node, level)

        # extra:
        level_wise_sum = [0 for _ in range(100005)] # max nodes => 10^5
        level_wise_sum[1] = root.val
        max_level = 0

        while q:
            top = q.pop(0)
            top_node, top_node_level = top[0], top[1]
            max_level = max(max_level, top_node_level)
    
            if top_node:
                if top_node.left:
                    q.append(
                        (top_node.left, top_node_level + 1)
                    )
                    level_wise_sum[top_node_level + 1] += top_node.left.val
                if top_node.right:
                    q.append(
                        (top_node.right, top_node_level + 1)
                    )
                    level_wise_sum[top_node_level + 1] += top_node.right.val
        
        # print(max_level, level_wise_sum[1: max_level+1])
        nums = level_wise_sum[1: max_level+1]
        h = []
        
        for num in nums:
            heappush(h, num * (-1)) # need MAX heap
        
        top = -1  
        while k:
            if h:
                top = heappop(h) * (-1)
            else:
                top = -1 
                break
            k -= 1
        
        return top