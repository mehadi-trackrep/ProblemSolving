from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
        1. Using 2pointer / fast-slow pointer find the middle node of the list.
        2. Now call mergeSort for 2 halves.
        3. Merge the Sort List (divide and conqueror Approach)
        
            ==> Divide & conquere approach use repeteadly divide at middle of each
        segment and then merge left & right.
        
        And we can find the `middle` position in linkedlist by using `slow-fast`
        two pointers approach!!
    """
    def mergeTwoList(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if not head1:
            return head2
        if not head2:
            return head1

        # we have both of the head1 and head2 nodes
        first_node = head1
        if head1.val < head2.val:
            # first_node = head1
            head1 = head1.next
        else:
            first_node = head2
            head2 = head2.next
        
        cur = first_node
        
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
            
        return first_node

    def findingMiddleNode(self, head: Optional[ListNode])-> Optional[ListNode]:
        mid = head
        while mid and head.next:
            mid = mid.next
            head = head.next.next
        return mid

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # base condition
        # if last leaf node / NULL node then return
        if not head or not head.next: return head # [STEP - 1]
        
        # finding mid [STEP - 2]
        slow, fast = head, head
        temp = None

        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next

        temp.next = None # cut the first half from the 2nd half of linked list
        
        lh = self.sortList(head) # left half is the head (still)
        rh = self.sortList(slow) # right half is the fast pointer as fast reaches at Null / last node!
        
        return self.mergeTwoList(lh, rh) # [STEP - 3]