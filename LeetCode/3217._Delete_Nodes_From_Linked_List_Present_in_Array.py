from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        # nnums = set(nums) # make set for 'in' operator to get T.C. - O(1)

        nnums = {None} # unordered set
        for num in nums:
            nnums.add(num)

        isFirstTime = False
        new_head = None
        new_node = None
        node = head

        while node:
            val = node.val

            if not val in nnums: # have to delete
                if not isFirstTime:
                    new_head = ListNode(node.val)
                    isFirstTime = True
                    new_node = new_head
                else:
                    tnn = ListNode(node.val)
                    new_node.next = tnn
                    new_node = tnn
            node = node.next
        
        return new_head

if __name__=="__main__":
    obj = Solution()
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    
    head = node1
    nums = [1,2,3]
    
    new_head = obj.modifiedList(nums, head)
    print("================================================")
    while new_head:
        print(new_head.val)
        new_head = new_head.next