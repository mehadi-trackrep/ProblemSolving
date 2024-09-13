from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    
    """
        V.V.I. This solution will not work for some cases like:-
            head = [2,2,1]
            root = [2,null,2,null,2,null,1]
        When the current node's val & current head's val are not equal then we just shift the head to 0th index but
        the current node remains at same position. That's the wrong. We just skipped the internal nodes to checkup
        here. :D
        To overcome this issue, one way will be like to pass the current node pointer in dfs function iteratively
        when the first time it has matched.
        And if it breaks the sequence then we must pass the 2nd start position.
        Anyway, it's complex.
        
        So, simple way:-
            We will traverse the root tree, node by node and for each node, we will check whether it's possible
            to get the full head sequence start from this node. :) 
            O (n * n)
    """
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        cur_head = head
        
        def dfs(cur_root_node, cur_head):
            # base case
            if not cur_root_node:
                return False
            if not cur_head: # traversed all elements
                return True
            
            if cur_root_node.val != cur_head.val:
                cur_head = head
            if cur_root_node.val == cur_head.val:
                return dfs(cur_root_node.left, cur_head.next) or dfs(cur_root_node.right, cur_head.next)
            else:
                return dfs(cur_root_node.left, cur_head) or dfs(cur_root_node.right, cur_head)
        
        return dfs(root, cur_head)

class Solution:
    def is_matches_all_sequentially_from_this_root_node(self, curr_head, curr_root) -> bool:
        if curr_head.val != curr_root.val:
            return False
        # if the upper condition doesn't match means curr_head.val == curr_root.val
            # so, if the curr_head.next is NULL means, we have checked all the heads and matched.
        if not curr_head.next: return True
        ans = False
        if curr_root.left:
            ans |= self.is_matches_all_sequentially_from_this_root_node(curr_head.next, curr_root.left)
        if curr_root.right:
            ans |= self.is_matches_all_sequentially_from_this_root_node(curr_head.next, curr_root.right)
        return ans

    def dfs(self, head, curr_root) -> bool:
        ans = False
        if self.is_matches_all_sequentially_from_this_root_node(head, curr_root):
            return True
        if curr_root.left:
            ans |= self.dfs(head, curr_root.left)
        if curr_root.right:
            ans |= self.dfs(head, curr_root.right)
        return ans

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root: return False
        
        return self.dfs(head, root)