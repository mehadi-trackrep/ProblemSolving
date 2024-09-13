from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1:
    # T.C. - O(n * n) with optimised operations
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

            if not val in nnums: # have to delete ; O(n) #TODO: we can use binary-search: O(logN)
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


"""
    # If we use binary-search then T.C. - O(N * logN)
"""


class Solution:
    """
        Here, T.C. - O(N) cause we will use hash table.
    """
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        max_val = -1
        for num in nums:
            max_val = max(max_val, num)
        
        freq = [False] * (max_val + 1)
        for num in nums:
            freq[num] = True # this num exists - index is the num itself
        
        temp = ListNode()
        current = temp
        
        while head:
            if head.val >= len(freq) or freq[head.val]==False: # this head.val is missing in the nums list, have to keep
                current.next = head
                current = current.next
            head = head.next
        
        current.next = None
        return temp.next # here, the first node has no value, val=0 but the next has the acutual first element/node
        
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