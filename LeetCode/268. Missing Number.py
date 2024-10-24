from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        0000
        0001
        0010
        0011
        0100
        0101
        0110
        0111 (7)
        1000 (8)
        1001 (9)
        ... 
        
        V.V.I. -- We have a couple of approaches there.
            1) hashing -> TC - O(n), ASC - O(n)
            2) math summation of n numbers -> TC - O(n), ASC - O(1) [n(n+1)/2 - sum(given numbers)]
            3) sorting and checking -> TC - O(nlogn), ASC - O(1)
            4) xor -> 
        """
        ln = len(nums)
        nums.sort()
        
        if nums[0] != 0: return 0
        if nums[ln-1] != ln: return ln
        
        
        for i in range(1, ln):
            if nums[i] - nums[i-1] != 1:
                return nums[i] - 1
