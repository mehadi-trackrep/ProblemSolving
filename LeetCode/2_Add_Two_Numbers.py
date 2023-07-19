# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = l1
        list1 = []
        while node is not None:
            list1.append(node.val)
            node = node.next
        
        # print("\n----------------\n")

        node = l2
        list2 = []
        while node is not None:
            list2.append(node.val)
            node = node.next
        
        big_list = []
        ind = 0
        carray = 0
        len1 = len(list1)
        len2 = len(list2)
        max_len_list = max(len1, len2)
        
        while ind < max_len_list:
            list1_val, list2_val = 0, 0
            if ind < len1:
                list1_val = list1[ind]
            if ind < len2:
                list2_val = list2[ind]
            if (list1_val + list2_val + carray) >= 10:
                big_list.append((list1_val + list2_val + carray) - 10)
                carray = 1
            else:
                big_list.append(list1_val + list2_val + carray)
                carray = 0
            ind += 1
        if carray:
            big_list.append(1)

        length = len(big_list)
        ListNodeObj = ListNode()

        for ind in range(length-1, -1, -1):
            if ind == length-1:
                ListNodeObj = ListNode(val=big_list[ind]) # leaf node
            else:
                ListNodeObj = ListNode(val=big_list[ind], next=ListNodeObj) # next node!
        
        return ListNodeObj


if __name__ == "__main__":
    """

        Approach:
            At first, we have to make the "leaf" node then
            subsequently its parent node.
        And then we have to pass the first nodes as parameters into the function. :)
                l1: [1, 6, 4]
                l2: [4, 6, 1]
                ------------- (sum)
                ANS: [5, 2, 6]

            l1: [1, 6, 6]
            l2: [4, 6, 6]
            ------------- (sum)
            ANS: [5, 2, 3, 1]

    """
    """
        Input
            [9,9,9,9,9,9,9]
            [9,9,9,9]
            ---------------
            [8,9,9,9,0,0,0,1]
    """

    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9,0]
    ListNodeObj1, ListNodeObj2 = None, None ## AC!

    for ind in range(len(l1)-1, -1, -1):
        if ind == len(l1)-1:
            ListNodeObj1 = ListNode(val=l1[ind]) # leaf node
        else:
            ListNodeObj1 = ListNode(val=l1[ind], next=ListNodeObj1) # next node!

    for ind in range(len(l2)-1, -1, -1):
        if ind == len(l2)-1:
            ListNodeObj2 = ListNode(val=l2[ind]) # leaf node
        else:
            ListNodeObj2 = ListNode(val=l2[ind], next=ListNodeObj2) # next node!

    solutionobj = Solution()
    ans_ListNodeObj = solutionobj.addTwoNumbers(l1=ListNodeObj1, l2=ListNodeObj2)
    
    node = ans_ListNodeObj
    while node is not None:
        print(node.val)
        node = node.next