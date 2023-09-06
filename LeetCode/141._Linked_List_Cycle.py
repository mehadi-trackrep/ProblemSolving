from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def dfs(self, node: ListNode) -> bool:
        if not node:
            return False
        # print("node.val: {}".format(node.val))
        if node.val == None:
            return True
        node.val = None
        res = self.dfs(node.next)
        return res
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.dfs(head)

if __name__ == "__main__":
    obj = Solution()
    
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    # head.next.next.next.next = head.next

    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = head.next

    print(obj.hasCycle(head))
