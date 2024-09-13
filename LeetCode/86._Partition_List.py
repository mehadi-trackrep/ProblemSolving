from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None
        
        backup_head = head
        
        cur_node = ListNode()
        backup_cur_node = cur_node
        ans = cur_node
        
        while head:
            if head.val < x:
                cur_node.val = head.val
                cur_node.next = ListNode()
                cur_node = cur_node.next
            head = head.next
            
        while backup_head:
            if backup_head.val >= x:
                cur_node.val = backup_head.val
                cur_node.next = ListNode()
                cur_node = cur_node.next
            backup_head = backup_head.next
        
        while backup_cur_node and backup_cur_node.next:
            if backup_cur_node.next.next:
                backup_cur_node = backup_cur_node.next
            else:
                backup_cur_node.next = None
                break
    
        return ans

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None

        dummyless = ListNode()
        dummygreat = ListNode()
        less = dummyless # it's < elements
        great = dummygreat # it's >= elements

        while head:
            if head.val >= x:
                great.next = head
                great = great.next
            else:
                less.next = head
                less = less.next
            head = head.next

        less.next = dummygreat.next
        great.next = None

        return dummyless.next # cause 1st node is a dummy node!