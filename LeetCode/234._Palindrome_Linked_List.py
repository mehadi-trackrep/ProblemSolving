from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:     ## T.C - O(n), S.C - O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
            Suppose we couldn't change the direction of linkedlist.
            So, here, we will do -  
                1) go to the middle of the list using slow & fast
                2) reverse the second half
                3) compare the two halves (using two heads up to the middle position)
                4) again reverse the second half
            T.C. - O(n) & 
            S.C - O(1)
        """
        # 1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2)
        head2 = self.reverse_2nd_half(slow)
        ck = self.ck_is_palindrome(head, head2)
        _ = self.reverse_2nd_half(slow)  # not necessary for this particular problem

        return True if ck else False

    def reverse_2nd_half(self, slow):
        head = current = slow
        previous = follow = None
        while current:  # in the last iteration current & follow will be NULL.
            follow = current.next
            current.next = previous
            previous = current
            current = follow
        head = previous
        return head

    def ck_is_palindrome(self, head1, head2):
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True

