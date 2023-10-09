## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        first_node_flag, outer_loop_flag, mx = True, True, 100000
        first_node, head = None, None

        k = len(lists)

        while outer_loop_flag:
            pos = -1
            min_val = mx

            for i in range(k):
                if lists[i]:
                    if lists[i].val <= min_val:
                        pos = i
                        min_val = lists[i].val
            
            if pos == -1: 
                # print("--> min_val: ", min_val)
                outer_loop_flag = False

            if min_val != mx:
                lists[pos] = lists[pos].next
                new_node = ListNode(min_val)
                if first_node_flag:
                    first_node, head = new_node, new_node
                    first_node_flag = False
                else:
                    head.next = new_node
                    head = head.next
        
        return first_node