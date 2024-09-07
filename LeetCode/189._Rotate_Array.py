from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Approach:-
        --------
            1,2,3,4, 5,6,7 ; k = 3
            [7,6,5], [4,3,2,1]
             5,6,7,   1,2,3,4
            
            nums[:] =   nums[-k:] # reverse the k to ln-1 elements and put it in first
                            + 
                        nums[:-k] # reverse the 0 to k elements and put it in last
                        
                        and then concat
            N.B. k might be >= ln
                so, the new k will be k % ln
                    k = k % ln
        """
        ln = len(nums)
        k = k % ln
        
        nums[:] = nums[-k:] + nums[:-k]