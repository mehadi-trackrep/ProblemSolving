from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        total_nodes = 0
        first_node = head

        while temp:
            total_nodes += 1
            temp = temp.next
        
        cnt = 0
        prev = None
        while head:
            if cnt == (total_nodes - n):
                if cnt == 0:
                    first_node = head.next
                else:
                    prev.next = head.next
                break

            prev = head
            head = head.next
            cnt += 1

        return first_node

"""
    ##Another easy and optimised solution:-
            Solution (Two-Pointer, One-Pass)

    We are required to remove the nth node from the end of list. For this, we need to traverse N - n nodes from the start of the list, where N is the length of linked list. We can do this in one-pass as follows -

    Let's assign two pointers - fast and slow to head. We will first iterate for n nodes from start using the fast pointer.

    Now, between the fast and slow pointers, there is a gap of n nodes. Now, just Iterate and increment both the pointers till fast reaches the last node. The gap between fast and slow is still of n nodes, meaning that slow is nth node from the last node (which currently is fast).

    For eg. let the list be 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9, and n = 4.

    Step - 1:-  (Here, we have to pass total n (here, 4) numbers of edges)
        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> null
        ^slow               ^fast
        |<--gap of n nodes-->|
    
    => Now traverse till fast reaches end
    Step - 2:- 
        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> null
                                ^slow               ^fast
                                |<--gap of n nodes-->|
                                
    'slow' is at (n+1)th node from end.
    So just delete nth node from end by assigning slow -> next as slow -> next -> next (which would remove nth node from end of list).
    Since we have to delete the nth node from end of list (And not nth from the last of list!), we just delete the next node to slow pointer and return the head.

"""

if __name__ == "__main__":
    obj = Solution()
    # node5 = ListNode(5)
    # node4 = ListNode(4, node5)
    # node3 = ListNode(3, node4)
    # node2 = ListNode(2, node3)
    # node1 = ListNode(1, node2)


    node2 = ListNode(2)
    node1 = ListNode(1, node2)
    head = node1

    temp = head
    while temp:
        print(temp.val)
        temp = temp.next

    new_head = obj.removeNthFromEnd(head, n=2)

    print("================================================")
    while new_head:
        print(new_head.val)
        new_head = new_head.next
