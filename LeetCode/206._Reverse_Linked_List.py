from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev, first_node = head, head # tortoise
        head = head.next # hare
        last_node = None

        while head:
            last_node = head # cause the head will be None at the end, that's why we have to keep track of the last node separately
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        first_node.next = None # to avoid cycle
        
        return last_node if last_node else first_node

class Solution: ### V.V.I.
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

if __name__ == "__main__":
    obj = Solution()

    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    head = node1

    temp = head
    while temp:
        print(temp.val)
        temp = temp.next

    new_head = obj.reverseList(head)

    print("================================================")
    while new_head:
        print(new_head.val)
        new_head = new_head.next