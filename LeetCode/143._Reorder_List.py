from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp, first_node = head, head
        arr = []
        
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        arr = arr[::-1]
        iters = len(arr) // 2
        
        '''
            When we have n(total nodes) = odd then we have to add/push n//2 times values
            But when we have n(total nodes) = even then we have to add/push n//2 - 1 times values
                where the last node next will be handled gracefully!
        '''
        is_even = False
        if len(arr)%2 == 0: # means even
            is_even = True

        for i in range(iters):
            if i == iters-1 and is_even:
                head = head.next
                break
            else:
                head = self.push(head, arr[i])
        
        head.next = None

        return first_node
    
    def push(self, head, a_value) -> Optional[ListNode]: # push at the next of current head
        new_node = ListNode(a_value)
        new_node.next = head.next
        temp = head.next
        head.next = new_node
        head = temp
        return head

class Solution: ## optimised without using any external array! else the code is same as above
    def reorderList(self, head):
        #step 1: find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt    
        slow.next = None
        
        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt

if __name__ == "__main__":
    obj = Solution()

    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    # node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    head = node1

    temp = head
    while temp:
        print(temp.val)
        temp = temp.next

    new_head = obj.reorderList(head)

    print("================================================")
    while new_head:
        print(new_head.val)
        new_head = new_head.next