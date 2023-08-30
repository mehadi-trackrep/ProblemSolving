from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1
        
        flag = False
        first_node, head = None, None

        while list1 and list2:
            new_node = None
            if list1.val <= list2.val:
                # print("==> list1.val: ", list1.val)
                new_node = ListNode(list1.val)
                list1 = list1.next
            else:
                # print("--> list2.val: ", list2.val)
                new_node = ListNode(list2.val)
                list2 = list2.next
            if not flag:
                # print("-=-=-=-=-=> new_node.val: ", new_node.val)
                first_node, head = new_node, new_node
                flag = True
            else:
                head.next = new_node
                head = head.next
        
        # print("----------------------------------------------------")
        ## for resedue
        while list1:
            # print("==> list1.val: ", list1.val)
            new_node = ListNode(list1.val)
            head.next = new_node
            head = head.next
            list1 = list1.next
        while list2:
            # print("--> list2.val: ", list2.val)
            new_node = ListNode(list2.val)
            head.next = new_node
            head = head.next
            list2 = list2.next
        
        return first_node

if __name__ == "__main__":
    obj = Solution()

    node3 = ListNode(4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    
    list1 = node1

    node3_ = ListNode(4)
    node2_ = ListNode(3, node3_)
    node1_ = ListNode(1, node2_)
    
    list2 = node1_

    new_head = obj.mergeTwoLists(list1, list2)

    while new_head:
        print(new_head.val)
        new_head = new_head.next